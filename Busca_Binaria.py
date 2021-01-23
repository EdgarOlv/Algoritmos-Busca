lista = list(range(0,10))

def busca_binaria(vetor, PosicaoInicial, PosicaoFinal, ElementoProcurado):
    # condição de existência
    if PosicaoInicial <= PosicaoFinal:
        meio = (PosicaoInicial + PosicaoFinal) // 2
        if ElementoProcurado > vetor[meio]:
            return busca_binaria(vetor, meio+1, PosicaoFinal, ElementoProcurado)
        elif ElementoProcurado < vetor[meio]:
            return busca_binaria(vetor, PosicaoInicial, meio-1, ElementoProcurado)
        else:
            return meio
    # não encontramos o elemento
    return None 

print(busca_binaria(lista,0,len(lista)-1,20))
