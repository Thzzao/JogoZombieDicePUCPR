''' Jogo criado para fins educacionais
    Desenvolvido por: Thiago Josinaldo
    dos Santos Souza.
    Aluno do curso de: ADS 2021/2        
'''

#Entrada de dados (Boas vindas)

print ("PROTÓTIPO FINAL")
nome = str(input("Qual seu nome?: "))
mensagem_boas_vindas = "Olá, %s bem vindo ao jogo Zombie Dice\n" %nome
print (mensagem_boas_vindas)

jogadores = 0

while jogadores < 2:
    jogadores = int(input("Quantos jogadores irão jogar?: "))

    if jogadores < 2:
        print("AVISO: Você precisa de pelo menos 2 jogadores!")

if jogadores > 1:
    regras = input("Gostaria de ler as regras do jogo? (s para SIM ou n para NÃO):")
    if regras == "s":
        print ( "Visite as regras no site: www.galapagosjogos.com.br e se prepare para comer alguns cérebros\n")
    else:
        print("\nPrepare-se para comer alguns cérebros.\n")

    print("Iniciando...\n")
    import time
    time.sleep(2)

#Início do jogo

    listaJogadores = []
    for i in range(jogadores):
        nomeJogadores = input("Informe o nome do jogador " + str(i + 1) + ": ")
    listaJogadores.append({"nome":nome, "cerebros":0})
### criar um dicionário para armazenar as pntuação de cada jogador

    #pontuacaoJogador = {jogador}


### mostrar quais dados tem no copo e atualizar a cada jogada quais dados ainda restam no copo( imprimiar a cada turno)
    input("\nAperte ENTER para sortear os dados")


#Criação das váriasveis do contador
    cerebros = 0
    passos = 0
    tiros = 0

#Criação dos dados

    dadoVerde = ( "C", "P", "C", "T", "P", "C")
    dadoAmarelo = ( "T", "P", "C", "T", "P", "C")
    dadoVermelho = ( "T", "P", "T", "C", "P", "T")

### fazer uma lista original para armazenar quando reiniciar o jogador, e uma copia para remover os itens
    listaDados = [
        dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,
        dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoAmarelo,
        dadoVermelho,dadoVermelho,dadoVermelho,
    ]

    jogadorAtual = 0
    dadosSorteados = []
    import random
### alterar o sorteio
    while True:
        print("\nHora do jogador ", listaJogadores[jogadorAtual])

        for i in range(0,3):
            numSorteado = random.randint(0, len(listaDados))# Zero conta como número

### mudar função randit para len, pois retirando os dados o numero da lista muda

### fazer a remoção dos dados sorteados da lista
            dadoSorteado = listaDados[numSorteado]

            if dadoSorteado == "CPCTPC":
                corDado = "Verde"
            elif dadoSorteado == "TPCTPC":
                corDado = "Amarelo"
            else:
                corDado = "Vermelho"

            print("O dado sorteado foi:",corDado)

            dadosSorteados.append(dadoSorteado)

        print("\nAs faces sorteadas foram: ")

        for dadoSorteado in dadosSorteados:
            faceDado = random.randint(0,5)

            if dadoSorteado [faceDado] == "C":
                print ("C - Você comeu um CÉREBRO")
                cerebros = cerebros + 1
            elif dadoSorteado [faceDado] == "T":
                print ("T - Você levou um TIRO")
                tiros = tiros + 1
            else:
                print ("P - Uma vítima escapou")
                passos = passos + 1
            #FIMSE
        #FIMPARA

#Contador de pontos

        mensagem_dados = "C = cérebro P = passos T = tiro\n"
        print ("\nPontuação atual:")
        print ("C:", cerebros)
        print ("T:", tiros)
        print ("P:", passos)
        print(mensagem_dados)

#Turno de cada jogador
        continuarTurno = input("AVISO: Você gostaria de jogar mais um dado? (s = SIM / n = NÃO):")
        if (continuarTurno == "n"):
            jogadorAtual = jogadorAtual + 1
            dadosSorteados = []
            tiros = 0
            carebros = 0
            passos = 0

        else:
            print ("Iniciando mais uma rodada do jogador: ", listaJogadores[jogadorAtual])
            time.sleep(2)
            dadosSorteados = []

### estabelecer as regras do jogo
### Arrumar a sequencia dos jogadores
