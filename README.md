
# minopt
[![Build Status](https://travis-ci.org/AjayMT/minopt.svg)](https://travis-ci.org/AjayMT/minopt)

A minimalistic option parser for Python inspired by substack's [minimist](http://github.com/substack/minimist) for node.js.

## API
### minopt(argv[, opts]])
This function takes a list of strings and parses them as if they were sys.argv.

Example:
```python
# example.py

import sys
from minopt import minopt

argv = minopt(sys.argv[1:])
print argv
```
```sh
$ python example.py --foo bar -raz --quux=riff hello --flag -f
{'a': True, 'z': True, 'f': True, 'quux': 'riff', 'flag': True, 'r': True, 'foo': 'bar', '_': ['hello']}
```

This function returns a dictionary that maps named arguments to their string values (or `True`, in the case of flags). It maps `_` to a list of unnamed arguments.

`argv` is a list of strings to be parsed as a list of arguments. `opts` is an optional argument and a dictionary with the following keys:
- `string`: a list of arguments to always be treated as strings
- `boolean`: a list of arguments to always be treated as flags

## Installation
```sh
$ python setup.py install
```

or

```sh
$ easy_install minopt
```

## Running tests
You'll need [pyvows](http://pyvows.org).
```sh
$ pyvows
```

## License
MIT License. See `./LICENSE` for details.
