from enum import Enum
from io import StringIO


class JKP(Enum):
    Pedra = 1
    Papel = 2
    Tesoura = 3


oponente = dict(A=JKP.Pedra,
                B=JKP.Papel,
                C=JKP.Tesoura)

eu = dict(X=JKP.Pedra,
          Y=JKP.Papel,
          Z=JKP.Tesoura)

def vence(m):
    if m == JKP.Pedra:
        return JKP.Papel
    elif m == JKP.Papel:
        return JKP.Tesoura
    else:
        return JKP.Pedra

def empata(m):
    return m

def perde(m):
    if m == JKP.Pedra:
        return JKP.Tesoura
    elif m == JKP.Papel:
        return JKP.Pedra
    else:
        return JKP.Papel

frauda = dict(X=perde,
              Y=empata,
              Z=vence)

def pontuacao_total(input):
    it = StringIO(input) if type(input) == str else input

    pontuacao = 0
    for n in it:
        o, _, e = n.strip()
        pontuacao += resultado_partida(oponente[o], eu[e])

    return pontuacao

def pontuacao_total_fraudada(input):
    it = StringIO(input) if type(input) == str else input

    pontuacao = 0
    for n in it:
        o, _, f = n.strip()
        pontuacao += resultado_partida(oponente[o], frauda[f](oponente[o]))

    return pontuacao

def resultado_partida(o, e):
    if (o, e) == (JKP.Pedra, JKP.Tesoura):
        pontos = 0
    elif (o, e) == (JKP.Papel, JKP.Pedra):
        pontos = 0
    elif (o, e) == (JKP.Tesoura, JKP.Papel):
        pontos = 0
    elif (o, e) == (JKP.Tesoura, JKP.Pedra):
        pontos = 6
    elif (o, e) == (JKP.Pedra, JKP.Papel):
        pontos = 6
    elif (o, e) == (JKP.Papel, JKP.Tesoura):
        pontos = 6
    else:
        pontos = 3

    return pontos + e.value


