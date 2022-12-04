from aoc2022 import dia1


class TestDia1:
    exemplo = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    def test_retorna_elfo_carregando_maior_quantidade_calorias(self):
        esperado = 4
        assert esperado == dia1.maior_quantidade_calorias(self.exemplo)[1]

    def test_retorna_soma_tres_maiores_quantidades_calorias(self):
        esperado = 45_000
        assert esperado == dia1.soma_tres_maiores_quantidades_calorias(self.exemplo)
