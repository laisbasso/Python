def éPrimo(x):
    if (x == 2):
        return True

    fator = 2
    while (x % fator != 0 and fator <= x/2):
        fator = fator + 1
    if (x % fator == 0):
        return False
    else:
        return True        

def primo(x):
    if éPrimo(x):
        print (x, 'é um número primo')
    else:
        print (x, 'não é um número primo')
