from aoc2022 import dia3


class TestDia2:
    exemplo = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

    def test_retorna_soma_prioridades(self):
        esperado = 157
        assert esperado == dia3.soma_prioridades(self.exemplo)

    def test_retorna_soma_prioridades_grupos(self):
        esperado = 70
        assert esperado == dia3.soma_prioridades_grupos(self.exemplo)
