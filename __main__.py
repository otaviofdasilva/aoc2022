if __name__ == "__main__":
    import sys
    from aoc2022.dia5 import topo_pilhas, topo_pilhas_9001

    with open(sys.argv[1], "r") as f:
        print(topo_pilhas(f))

    with open(sys.argv[1], "r") as f:
        print(topo_pilhas_9001(f))
