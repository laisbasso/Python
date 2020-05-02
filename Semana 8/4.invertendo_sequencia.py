print('Digite uma sequência de números. Para finalizar digite 0.')
lista = []
n = 1
while (n != 0):
    n = int(input('Digite um número: '))
    lista.append(n)
lista.pop()
lista.reverse()
for i in lista:
    print(i)
