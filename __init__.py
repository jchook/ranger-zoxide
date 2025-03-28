import os.path
import ranger.api
import ranger.core.fm
import ranger.ext.signals
from subprocess import Popen, PIPE, run

hook_init_prev = ranger.api.hook_init

def hook_init(fm):
    def zoxide_add(signal):
        Popen(["zoxide", "add", signal.new.path])

    fm.signal_bind("cd", zoxide_add)
    fm.commands.alias("zi", "z -i")
    return hook_init_prev(fm)


ranger.api.hook_init = hook_init

class z(ranger.api.commands.Command):
    """
    :z

    Jump around with zoxide (z)
    """
    def execute(self):
        results = self.query(self.args[1:])

        input_path = ' '.join(self.args[1:])
        if not results and os.path.isdir(input_path):
            self.fm.cd(input_path)
            return

        if not results:
            return

        if os.path.isdir(results[0]):
            self.fm.cd(results[0])

    def query(self, args):
        try:
            zoxide = self.fm.execute_command(["zoxide", "query", "--exclude", self.fm.thisdir.path, *self.args[1:]],
                                             stdout=PIPE)
            stdout, stderr = zoxide.communicate()

            if zoxide.returncode == 0:
                output = stdout.decode("utf-8").strip()
                return output.splitlines()
            elif zoxide.returncode == 1: # nothing found
                return None
            elif zoxide.returncode == 130: # user cancelled
                return None
            else:
                output = stderr.decode("utf-8").strip() or f"zoxide: unexpected error (exit code {zoxide.returncode})"
                self.fm.notify(output, bad=True)
        except Exception as e:
            self.fm.notify(e, bad=True)

    def tab(self, tabnum):
        results = self.query(self.args[1:])
        return ["z {}".format(x) for x in results]

