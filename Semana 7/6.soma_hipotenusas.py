def é_hipotenusa(n):
    hipotenusas = []
    contador = 1
    i = 1
    j = 1
    
    while (contador <= n):
        while (i < n):
            while (j < n):
                if (contador**2 == i**2 + j**2):
                    if (hipotenusas == [] or hipotenusas[-1] != contador):
                        hipotenusas.append(contador)
                j = j + 1
            j = 1
            i = i + 1
        j = 1
        i = 1
        contador = contador + 1
    return hipotenusas

def soma_hipotenusas(n):
    hipotenusas = é_hipotenusa(n)
    index = 0
    soma = 0
    while (index < len(hipotenusas)):
        soma = soma + hipotenusas[index]
        index = index + 1
    return soma
