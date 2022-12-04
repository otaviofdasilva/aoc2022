if __name__ == "__main__":
    import sys
    from aoc2022.dia3 import soma_prioridades, soma_prioridades_grupos

    with open(sys.argv[1], "r") as f:
        print(soma_prioridades(f))

    with open(sys.argv[1], "r") as f:
        print(soma_prioridades_grupos(f))
