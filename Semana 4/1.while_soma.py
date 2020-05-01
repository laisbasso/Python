seq = int(input("Quantos números você quer somar? "))
c = 1
soma = 0
while (c <= seq):
    num = int(input('Digite o '+ str(c)+ 'º número: '))
    soma = soma + num
    c = c + 1
print("A soma dos números é igual a", soma)
