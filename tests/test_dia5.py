from aoc2022 import dia5


class TestDia5:
    exemplo = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

    def test_retorna_topo_pilhas(self):
        esperado = "CMZ"
        assert esperado == dia5.topo_pilhas(self.exemplo)

    def test_retorna_topo_pilhas_9001(self):
        esperado = "MCD"
        assert esperado == dia5.topo_pilhas_9001(self.exemplo)
