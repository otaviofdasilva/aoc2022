if __name__ == '__main__':
    import sys
    from aoc2022.dia2 import pontuacao_total, pontuacao_total_fraudada

    with open(sys.argv[1], 'r') as f:
        print(pontuacao_total(f))

    with open(sys.argv[1], 'r') as f:
        print(pontuacao_total_fraudada(f))
        
