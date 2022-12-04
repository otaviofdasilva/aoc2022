from aoc2022 import dia4


class TestDia4:
    exemplo = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

    def test_retorna_numero_intervalos_completamente_contidos(self):
        esperado = 2
        assert esperado == dia4.numero_intervalos_completamente_contidos(self.exemplo)

    def test_retorna_numero_intervalos_parcialmente_contidos(self):
        esperado = 4
        assert esperado == dia4.numero_intervalos_parcialmente_contidos(self.exemplo)
