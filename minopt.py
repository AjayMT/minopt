
def _minopt_getarg(arg):
    if arg[:2] == '--':
        return [arg[2:]]

    return list(arg[1:])


def minopt(argv, opts={'string': [], 'boolean': []}):
    """Parse a list of command-line arguments.

    Argmuents:
    argv -- A list of command-line arguments (strings)
    opts -- A dictionary with keys 'string' and 'boolean'
      which are mapped to a list of arguments to always be
      treated as strings and flags respectively
    """
    opts['string'] = [] if 'string' not in opts else opts['string']
    opts['boolean'] = [] if 'boolean' not in opts else opts['boolean']

    args = {}
    optargs = {i: a for i, a in enumerate(argv) if a[0] == '-'}
    args['_'] = {i: a for i, a in enumerate(argv) if not a[0] == '-'}

    for n in optargs:
        arg = _minopt_getarg(optargs[n])
        for a in arg:
            val = None
            if '=' in a:
                val = a.split('=')[1]
                a = a.split('=')[0]

            isnotbool = a not in opts['boolean']
            isnotstr = a not in opts['string']
            if not val:
                if (n + 1) in args['_']:
                    args[a] = args['_'].pop(n + 1) if isnotbool else True
                else:
                    args[a] = True if isnotstr else ''
            else:
                args[a] = val if isnotbool else True

    unnamed = args['_']
    args['_'] = [unnamed[i] for i in sorted(unnamed)]

    for a in opts['boolean'] + opts['string']:
        if a not in args:
            args[a] = False if a in opts['boolean'] else ''

    return args
