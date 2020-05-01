def éPrimo(x):
    contador = 2
    primos = 1
    while (contador <= x):
        fator = 2
        while (contador % fator != 0 and fator <= contador/2):
            fator = fator + 1
        if (contador % fator != 0):
            primos = primos + 1
        contador = contador + 1
    return primos

def n_primos(x):
    return éPrimo(x)
        
