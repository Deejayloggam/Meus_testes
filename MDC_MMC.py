def mmc(iteravel):
    """
    recebe um iterável (números)
    retorna o minimo multiplo comum
    """
    contador = 0
    multiplicacoes = []
    while True:
        contador += 1
        for n in iteravel:
            multiplicacoes.append(contador*n)
        for n in multiplicacoes:
            cont = multiplicacoes.count(n)
            if cont == len(iteravel):
                return n


def mdc(iteravel):
    """
    recebe um iterável (números)
    retorna o máximo divisor comum entre os mesmos
    """
    divisor = int
    iteravel_organizado = sorted(iteravel)
    for n in range(iteravel_organizado[-1], 0, -1):
        cont = 0
        for n2 in iteravel_organizado:
            if n2 % n == 0:
                cont += 1
        if cont == len(iteravel_organizado):
            divisor = n
            break
    return divisor
