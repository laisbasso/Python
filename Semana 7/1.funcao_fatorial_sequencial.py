def fatorial_sequencial(n):
    fat = 1
    ni = n
    while n > 1:
        fat = fat * n
        n = n - 1
    print('O fatorial de ' + str(ni) + ' é ' + str(fat))

n = int(input('Digite um número positivo para calcular seu fatorial: '))
while n >= 0:
    fatorial_sequencial(n)
    n = int(input('Digite um número positivo para calcular seu fatorial: '))
