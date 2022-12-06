if __name__ == "__main__":
    import sys
    from aoc2022.dia6 import (
        posicao_primeiro_marcador,
        posicao_primeiro_marcador_mensagem,
    )

    with open(sys.argv[1], "r") as f:
        print(posicao_primeiro_marcador(f.readline()))

    with open(sys.argv[1], "r") as f:
        print(posicao_primeiro_marcador_mensagem(f.readline()))
