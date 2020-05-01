lista = []
print('Digite uma sequência de números. Para finalizar digite 0.')
n = 1
while (n != 0):
    n = int(input('Digite um número: '))
    lista.append(n)

index = len(lista)-1
while (index >= 0):
    print(lista[index])
    index = index - 1 
