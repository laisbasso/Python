seq = 1
ult = 1
adjacente = False

seq = int(input('Digite uma sequência: '))
if (seq // 10) > 0:
    while seq > 0 and adjacente == False:
        ult = seq % 10
        seg = (seq // 10) % 10
        if ult == seg:
            adjacente = True
        else:
            seq = seq//10

if adjacente:
    print('A sequências contém números adjacentes iguais.')
else:
    print('A sequências não contém números adjacentes iguais.')
