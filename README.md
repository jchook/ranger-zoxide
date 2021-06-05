# ranger-zoxide

A [`zoxide`](https://github.com/ajeetdsouza/zoxide) (aka `z`) plugin for
[`ranger`](https://github.com/ranger/ranger).

Easily jump between commonly visited directories by running this in ranger:

```
:z <partial-name>
```

## Features

- Very simple &amp; fast thanks to zoxide
- Supports tab completion
- Works with Python >= 2.7, or >= 3.1

## Install via Git

Clone this repository into your `~/.config/ranger/plugins` folder. For example:

```sh
git clone git@github.com:jchook/ranger-zoxide.git ~/.config/ranger/plugins/zoxide
```

## Keyboard Shortcut

You may wish to add a keyboard shortcut to quickly `z` between common
directories. Simply add a binding to your `~/.config/ranger/rc.conf` file:

```
map cz console z%space
```

## See Also

- [zoxide/contrib/ranger.py](https://github.com/ajeetdsouza/zoxide/blob/master/contrib/ranger.py)
- [ranger-zjumper](https://github.com/ask1234560/ranger-zjumper).

## License

MIT
