# Dialite

[![Build Status](https://travis-ci.org/flexxui/dialite.svg)](https://travis-ci.org/flexxui/dialite)
[![Documentation Status](https://readthedocs.org/projects/dialite/badge/?version=latest)](https://dialite.readthedocs.org)

Dialite is a lightweight Python package to show dialogs. It provides a
handful of functions, each a verb, that can be used to `inform()`, `warn()`
or `fail()` the user, or to `ask_ok()`, `ask_retry()` or `ask_yesno()`.

Dialite is pure Python, has no dependencies, and is written to work on
Python 3 and Python 2.7. It works on Windows (from at least XP), Linux
(most ones anyway, including Raspbian) and OS X.

Dialite provides a way to communicate with the user without needing a fancy
(and heavy) GUI library. It's also much easier to package with tools like
cx_Freeze and PyInstaller.


## Example:
    
```py
import dialite

res = dialite.ask_yesno('Troll question', 'Do you prefer VI over Emacs?')

if dialite.ask_ok('Confirm download', 'Will now download the resources.'):
    ...
```


## Installation

`pip install dialite`


## License

BSD 2-clause. See LICENSE for details.
