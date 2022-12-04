if __name__ == "__main__":
    import sys
    from aoc2022.dia4 import (
        numero_intervalos_completamente_contidos,
        numero_intervalos_parcialmente_contidos,
    )

    with open(sys.argv[1], "r") as f:
        print(numero_intervalos_completamente_contidos(f))

    with open(sys.argv[1], "r") as f:
        print(numero_intervalos_parcialmente_contidos(f))
