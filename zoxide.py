from ranger.api.commands import Command
from subprocess import check_output, CalledProcessError

class z(Command):
    """
    :z

    Jump around with zoxide (z)
    """
    def execute(self):
        results = self.query(self.args[1])
        self.fm.cd(results[0])

    def query(self, req):
        try:
            return check_output(['zoxide', 'query', req]).splitlines()
        except CalledProcessError as e:
            if e.returncode == 1:
                self.fm.notify("No matches found", bad=True)
            else:
                self.fm.notify("zoxide exited with status: %i".format(e.returncode), bad=True)
        except Exception as e:
            self.fm.notify("zoxide not found", bad=True)

    def tab(self, tabnum):
        results = self.query(self.args[1])
        return ["z {}".format(x) for x in results]
