if __name__ == '__main__':
    import sys
    from aoc2022.dia1 import maior_quantidade_calorias, soma_tres_maiores_quantidades_calorias

    with open(sys.argv[1], 'r') as f:
        print(maior_quantidade_calorias(f))

    with open(sys.argv[1], 'r') as f:
        print(soma_tres_maiores_quantidades_calorias(f))
        
