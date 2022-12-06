from aoc2022 import dia6


class TestDia6:
    exemplo = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

    def test_retorna_posicao_primeiro_marcador(self):
        esperado = 11
        assert esperado == dia6.posicao_primeiro_marcador(self.exemplo)

    def test_retorna_posicao_primeiro_marcador_mensagem(self):
        esperado = 26
        assert esperado == dia6.posicao_primeiro_marcador_mensagem(self.exemplo)
