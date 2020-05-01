def inicio():
    print("Bem vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    resposta_partida = int(input("2 - para jogar um campeonato "))
    print()

    while (resposta_partida < 1 or resposta_partida > 2):
        print("Oops! Opção inválida! Tente de novo.")
        print()
        print("1 - para jogar uma partida isolada")
        resposta_partida = int(input("2 - para jogar um campeonato "))
        if (resposta_partida == 1 or resposta_partida == 2):
            break

    if (resposta_partida == 1):
        print("Você escolheu uma partida!")
        print()
        partida()
        placar(resposta_partida)
    else:
        print("Você escolheu um campeonato!")
        campeonato(0)
        placar(resposta_partida)

def campeonato(rodada_campeonato):
    while (rodada_campeonato < 3):
        rodada_campeonato = rodada_campeonato + 1
        print()
        print("**** Rodada " + str(rodada_campeonato) + " ****")
        partida()

def partida():
    print()
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while (n < m):
        print("Opção inválida! O primeiro valor deve ser maior que o segundo!")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if (n > m):
            break
    print()

    if (n % (m+1) == 0):
        print("Você começa!")
        jogador = 1
    else:
        print("Computador começa!")
        jogador = 2
    print()

    while (n > 0):
        if (jogador % 2 != 0):
            n = n - usuario_escolhe_jogada(n, m)
            status(n, m)
        else:
            n = n - computador_escolhe_jogada(n, m)
            if (n > 0):
                status(n, m)        
        jogador = jogador + 1
    print("Fim do jogo! O computador ganhou!")

def status(n, m):
    if (n == 1):
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print("Agora restam " + str(n) + " peças no tabuleiro.")
    print()

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    print()

    while (jogada < 1 or jogada > n or jogada > m):
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
        if (jogada >= 1 and jogada <= m):
            break

    if (jogada > 1 and jogada <= m):
        print("Você tirou " + str(jogada) + " peças.")
    else:
        print("Você tirou uma peça.")
    print()
    return jogada

def computador_escolhe_jogada(n, m):
    jogada = 1
    resto = n - jogada
    while (resto % (m+1) != 0):
        jogada = jogada + 1
        resto = n - jogada
        if (resto % (m+1) == 0 or jogada > m):
            break
    if (jogada > m):
        jogada = m        

    if (jogada == 1):
        print("O computador tirou uma peça.")
    if (jogada > 1 and jogada <= m):
        print("O computador tirou " + str(jogada) + " peças.")
    return jogada

def placar(resposta_partida):
    if (resposta_partida == 1):
        resposta_partida = "da partida"
        n = 1
    else:
        resposta_partida = "do campeonato"
        n = 3
    print("**** Final " + resposta_partida + "! ****")
    print()
    print("Placar: Você 0 X " + str(n) + " Computador")

inicio()
