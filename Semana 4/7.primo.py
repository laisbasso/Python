n = int(input('Digite um número inteiro: '))
c = n
primo = True

while (c > 2):
    c = c - 1
    if (n % c == 0):
        primo = False

if primo == True:
    print('primo')
else:
    print('não primo')
