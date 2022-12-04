from aoc2022 import dia2


class TestDia2:
    exemplo = """A Y
B X
C Z
"""

    def test_retorna_pontuacao_total(self):
        esperado = 15
        assert esperado == dia2.pontuacao_total(self.exemplo)

    def test_retorna_pontuacao_total_fraudada(self):
        esperado = 12
        assert esperado == dia2.pontuacao_total_fraudada(self.exemplo)
