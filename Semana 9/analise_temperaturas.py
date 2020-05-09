def analise_temperaturas(lista_temperaturas):
    print("Temperatura máxima =", analise_maxima(lista_temperaturas))
    print("Temperatura mínima =", analise_minima(lista_temperaturas))

def analise_maxima(lista_temperaturas):
    temperatura_maxima = lista_temperaturas[0]
    for temperatura in lista_temperaturas:
        if temperatura > temperatura_maxima:
            temperatura_maxima = temperatura       
    return temperatura_maxima

def analise_minima(lista_temperaturas):
    temperatura_minima = lista_temperaturas[0]
    for temperatura in lista_temperaturas:
        if temperatura < temperatura_minima:
            temperatura_minima = temperatura
    return temperatura_minima

def teste_pontual_max(temp, valor_esperado):
    valor_calculado = analise_maxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("Valor esperado:", valor_esperado)
        print("Valor calculado:", valor_calculado)

def teste_pontual_min(temp, valor_esperado):
    valor_calculado = analise_minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("Valor esperado:", valor_esperado)
        print("Valor calculado:", valor_calculado)

def teste_maxima():
    print("Iniciando os testes")
    teste_pontual_max([0], 0)
    teste_pontual_max([0, 0, 0, 0, 0, 0], 0)
    teste_pontual_max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    teste_pontual_max([28, 30, 28, 26, 28, 31, 24, 20, 23, 24, 22, 23, 27, 23, 26,
                   27, 20, 24, 23, 25, 25, 25, 25, 26, 28, 28, 25, 26, 27, 27], 31)
    teste_pontual_max([-15, -12, 0, 20, 30], 30)
    print("Finalizando os testes")        

def teste_minima():
    print("Iniciando os testes")
    teste_pontual_min([0], 0)
    teste_pontual_min([0, 0, 0, 0, 0, 0], 0)
    teste_pontual_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual_min([28, 30, 28, 26, 28, 31, 24, 20, 23, 24, 22, 23, 27, 23, 26,
                   27, 20, 24, 23, 25, 25, 25, 25, 26, 28, 28, 25, 26, 27, 27], 20)
    teste_pontual_min([-15, -12, 0, 20, 30], -15)
    print("Finalizando os testes")
