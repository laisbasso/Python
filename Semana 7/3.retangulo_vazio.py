largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

cont = 1
cheio = 1 
largura_inicial = largura
altura_inicial = altura
while altura > 0:
    largura = largura_inicial
    while largura > 0:
        if (cont == 1 or cont == altura_inicial):
            print('#', end='')
        else:
            if (cheio == 1 or cheio == (largura + 1)):
                print('#', end='')
                cheio = cheio + 1
            else:
                print(' ', end='')
        largura = largura - 1
    altura = altura - 1
    cont = cont + 1
    print()
    
