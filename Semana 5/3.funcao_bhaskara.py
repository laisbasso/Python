import math

def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    imprime_raizes(a,b,c)

def delta(a,b,c):
    return (b**2) - (4*a*c)

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if (d < 0):
        print('esta equação não possui raízes reais')
    else:
        raiz1= (-b + math.sqrt(d)) / (2*a)
        raiz2= (-b - math.sqrt(d)) / (2*a)
        if (d == 0):
            print('a raiz desta equação é', raiz1)
        else:
            if (raiz1 > raiz2):
                aux = raiz1
                raiz1 = raiz2
                raiz2 = aux
            print('as raízes da equação são', raiz1, 'e', raiz2)
