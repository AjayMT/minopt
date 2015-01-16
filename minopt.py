
def _minopt_getarg(arg):
    if arg[:2] == '--':
        return [arg[2:]]

    return list(arg[1:])


def minopt(argv, opts={'string': [], 'boolean': []}):
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

    return args
