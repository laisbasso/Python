seq = int(input('Digite uma sequência de números para somar: '))
soma = 0

while seq != 0:
    mod = seq % 10
    soma = soma + mod
    seq = seq // 10

print('O resultado da soma é', soma)
