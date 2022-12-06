def posicao_primeiro_marcador(input):
    return _marcador_sequencia_sem_repeticao(input, 4)


def posicao_primeiro_marcador_mensagem(input):
    return _marcador_sequencia_sem_repeticao(input, 14)


def _marcador_sequencia_sem_repeticao(seq, tamanho):

    for i in range(len(seq)):
        e = i + tamanho
        s = set(seq[i:e])
        if len(s) == tamanho:
            return e

    return None
