import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()
    
    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))    
    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
        print()
    
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(assinatura_calculada, assinatura_infectada):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    resultado_diferenca = []
    
    for i in range (0, assinatura_calculada.__len__(), 1):
        resultado_diferenca.append(abs(assinatura_infectada[i] - assinatura_calculada[i]))

    soma_diferenca = 0
    for resultado in resultado_diferenca:
        soma_diferenca += resultado

    grau_similaridade = soma_diferenca / 6

    return grau_similaridade

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    # wal_texto = Tamanho médio de palavra
    texto = texto.lower()
    total_letras = 0
    lista_palavras = []
    lista_frases = []
    
    lista_sentencas = separa_sentencas(texto)
    for sentenca in lista_sentencas:
      novas_frases = separa_frases(sentenca)
      lista_frases.extend(novas_frases)
      
    for frase in lista_frases:
      novas_palavras = separa_palavras(frase)
      lista_palavras.extend(novas_palavras)
      
    for palavra in lista_palavras:
      total_letras += palavra.__len__()
    
    wal_texto = total_letras / lista_palavras.__len__()
    
    # ttr_texto = Relação Type-Token
    ttr_texto = n_palavras_diferentes(lista_palavras) / lista_palavras.__len__()

    # hlr_texto = Razão Hapax Legomana
    hlr_texto = n_palavras_unicas(lista_palavras) / lista_palavras.__len__()
    
    # sal_texto = Tamanho médio de sentença
    caracteres_sentencas = 0
    for sentenca in lista_sentencas:
      caracteres_sentencas += sentenca.__len__()

    sal_texto = caracteres_sentencas / lista_sentencas.__len__()
    
    # sac_texto = Complexidade média da sentença
    sac_texto =  lista_frases.__len__() / lista_sentencas.__len__()
    
    # pal_texto = Tamanho médio de frase
    caracteres_frases = 0
    for frase in lista_frases:
      caracteres_frases += frase.__len__()

    pal_texto = caracteres_frases / lista_frases.__len__()
   
    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]

def avalia_textos(textos, assinatura_infectada):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinatura_texto = []
    lista_assinaturas = []
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        lista_assinaturas.append(compara_assinatura(assinatura_texto, assinatura_infectada))
    
    return lista_assinaturas.index(max(lista_assinaturas))

def main():
    
    assinatura_infectada = []
    assinatura_infectada = le_assinatura()
    
    textos = []
    textos = le_textos()

    print("O autor do texto " + str(avalia_textos(textos, assinatura_infectada)) + " está infectado com COH-PIAH.")
