from io import StringIO
from functools import reduce
from operator import mul, attrgetter


class Macaco:
    def __init__(self):
        self.preferido = None
        self.rejeitado = None
        self.mapa = lambda a, b: None
        self.itens = None
        self.numero_inspecoes = 0

    def recebe(self, item):
        self.itens.append(item)

    def inspeciona_itens(self):
        self.itens = list(map(_comp(lambda i: int(i // 3), self.mapa), self.itens))
        self.numero_inspecoes += len(self.itens)

    def joga_item(self, macacos):
        i = self.itens[0]

        self.itens.remove(i)

        if not (i % self.divisor):
            macacos[self.preferido].recebe(i)
        else:
            macacos[self.rejeitado].recebe(i)

    def __repr__(self):
        return f"Macaco(itens={self.itens}, numero_inspecoes={self.numero_inspecoes})"


def _comp(f, g):
    return lambda x: f(g(x))


def produto_macacos_mais_ativos(input, n, vezes):
    macacos = _parse(input)

    t = len(macacos)

    while vezes:
        i = 0

        while i < t:
            macaco = macacos[i]
            macaco.inspeciona_itens()

            while macaco.itens:
                macaco.joga_item(macacos)

            i += 1

        vezes -= 1

    numero_inspecoes = attrgetter("numero_inspecoes")
    n_maiores = sorted(map(numero_inspecoes, macacos))[-n:]
    resultado = reduce(mul, n_maiores)

    return resultado


def _parse(input):
    macacos = []

    def eval(code):
        left, op, right = code.split(" ")

        match op:
            case "+":
                return int(left) + int(right)
            case "*":
                return int(left) * int(right)

    def operacao(code):
        return lambda x: eval(code.replace("old", str(x)))

    it = (i.strip() for i in (StringIO(input) if type(input) == str else input))
    for i in it:
        if not macacos or not i:
            macacos.append(Macaco())

        elif i.startswith("Starting"):
            _, itens = i.split(": ")
            itens = list(map(int, itens.split(", ")))
            macacos[-1].itens = itens

        elif i.startswith("Operation"):
            _, op = i.split(": new = ")
            macacos[-1].mapa = operacao(op)

        elif i.startswith("Test"):
            divisor = int(i.replace("Test: divisible by ", ""))
            macacos[-1].divisor = divisor

            macacos[-1].preferido = int(
                next(it).replace("If true: throw to monkey ", "")
            )
            macacos[-1].rejeitado = int(
                next(it).replace("If false: throw to monkey ", "")
            )

    return macacos
