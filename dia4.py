from io import StringIO


def _parse_range(s):
    c, f = s.split("-")
    return range(int(c), int(f) + 1)


def _acumula(input, p):

    numero = 0
    for r in (i.strip() for i in input):
        fg, sg = map(lambda s: set(_parse_range(s)), r.split(","))

        uniao = fg.union(sg)
        if p(len(uniao), len(fg), len(sg)):
            numero += 1

    return numero


def numero_intervalos_completamente_contidos(input):
    it = StringIO(input) if type(input) == str else input

    return _acumula(it, lambda u, f, s: u in (f, s))


def numero_intervalos_parcialmente_contidos(input):
    it = StringIO(input) if type(input) == str else input

    return _acumula(it, lambda u, f, s: u < f + s)
