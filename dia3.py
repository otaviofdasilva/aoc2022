from io import StringIO


_items = [
    *map(chr, range(ord("a"), ord("z") + 1)),
    *map(chr, range(ord("A"), ord("Z") + 1)),
]


def soma_prioridades_grupos(input):
    it = StringIO(input) if type(input) == str else input

    soma = 0
    grupo = []
    for items in (items.strip() for items in it):

        if 3 > len(grupo):
            grupo.append(set(items))
        else:
            i, *_ = grupo[0].intersection(grupo[1]).intersection(grupo[2])
            soma += _prioridade(i)
            grupo.clear()
            grupo.append(set(items))

    else:
        i, *_ = grupo[0].intersection(grupo[1]).intersection(grupo[2])
        soma += _prioridade(i)

    return soma


def soma_prioridades(input):
    it = StringIO(input) if type(input) == str else input

    soma = 0
    for items in (items.strip() for items in it):
        metade = len(items) // 2
        fh = set(items[:metade])
        sh = set(items[metade:])
        i, *_ = fh.intersection(sh)
        soma += _prioridade(i)

    return soma


def _prioridade(i):
    return _items.index(i) + 1
