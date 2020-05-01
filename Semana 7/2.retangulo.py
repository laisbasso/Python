largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

largura_inicial = largura
while altura > 0:
    largura = largura_inicial
    while largura > 0:
        print('#', end='')
        largura = largura - 1
    altura = altura - 1
    print()
    
