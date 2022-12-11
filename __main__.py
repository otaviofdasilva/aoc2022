if __name__ == "__main__":
    import sys
    from aoc2022.dia11 import *

    with open(sys.argv[1], "r") as f:
        print(produto_macacos_mais_ativos(f, 2, 20))

    """
    with open(sys.argv[1], "r") as f:
        print(f)
    """
