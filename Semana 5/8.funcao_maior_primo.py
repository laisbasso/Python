def éPrimo(x):
    contador = 2
    while (contador <= x):
        fator = 2
        while (contador % fator != 0 and fator <= contador/2):
            fator = fator + 1
        if (contador % fator != 0):
            maior = contador
        contador = contador + 1
    return maior

def maior_primo(x):
    if (x == 2):
        return x
    else:
        return éPrimo(x)
        
