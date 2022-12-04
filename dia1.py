from io import StringIO
from functools import reduce


def maior_quantidade_calorias(input):
    it = StringIO(input) if type(input) == str else input

    def r(acc, v):
        soma, indice_atual, maior, indice_maior = acc

        i = v.strip()

        if i:
            return soma + int(i), indice_atual, maior, indice_maior
        elif soma > maior:
            return 0, indice_atual + 1, soma, indice_atual
        else:
            return 0, indice_atual + 1, maior, indice_maior

    _, __, maior, indice = reduce(r, it, (0, 1, 0, 1))

    return maior, indice


def soma_tres_maiores_quantidades_calorias(input):
    it = StringIO(input) if type(input) == str else input

    soma = 0
    tres_maiores = []
    for n in it:
        i = n.strip()
        if i:
            soma += int(i)
        else:
            tres_maiores = _insere(tres_maiores, soma, 3)
            soma = 0

    tres_maiores = _insere(tres_maiores, soma, 3)
    return sum(tres_maiores)


def _insere(xs, x, max):
    ys = xs[:]
    ys.append(x)
    ys.sort()
    return ys[-max:]
