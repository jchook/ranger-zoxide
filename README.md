# ranger-zoxide

A [`zoxide`](https://github.com/ajeetdsouza/zoxide) (aka `z`) plugin for
[`ranger`](https://github.com/ranger/ranger).

Easily jump between commonly visited directories by running this in ranger:

```
:z <partial-name>
```

Or use interactive mode:

```
:zi <partial-name>
```

## Features

- Very simple &amp; fast thanks to zoxide
- Supports tab completion
- Works with Python >= 2.7, or >= 3.1

## Install

For ranger >= 1.9.3, use Git to clone this repository into your
`~/.config/ranger/plugins` folder. For example:

```sh
git clone git@github.com:jchook/ranger-zoxide.git ~/.config/ranger/plugins/zoxide
```

**Legacy Install**

For ranger versions older than 1.9.3, or to install without Git, download
`__init__.py` to your `~/.config/ranger/plugins` directory. For example:

```sh
mkdir -p ~/.config/ranger/plugins
wget -O ~/.config/ranger/plugins/zoxide.py https://raw.githubusercontent.com/jchook/ranger-zoxide/master/zoxide.py
```

## Keyboard Shortcut

You may wish to add a keyboard shortcut to quickly `z` between common
directories. Simply add a binding to your `~/.config/ranger/rc.conf` file:

```
map cz console z%space
```

Or for interactive use:

```
map cz zi
```

## See Also

- [ranger-zjumper](https://github.com/ask1234560/ranger-zjumper).

## License

MIT
