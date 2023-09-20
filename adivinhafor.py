import random

def jogar():

    print("\n*******************")
    print("Jogo da Adivinhação")
    print("*******************")

    random.seed(50)
    numsecreto = random.randrange(1,51)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade? (1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Insira o número da dificuldade: "))

    if(nivel==1):
        tentativas = 20
    elif(nivel==2):
        tentativas = 10
    else:
        tentativas = 5


    for rodada in range (1,tentativas+1): # a função range possui os parâmetros "range(start, stop, [step])"
        print("Tentativa {} de {}".format(rodada, tentativas)) # print("Tentativa", rodada, "de", tentativas)
        
        chute = input("\nDigite o seu número entre 1 e 50: ") #*******
        if(int(chute) < 1 or int(chute) > 50):
            print("\nVocê deve digitar um número entre 1 e 50")
            continue

        acertou = numsecreto == int (chute)
        maior = numsecreto > int (chute)
        menor = numsecreto < int (chute)
        errou = rodada == tentativas

        if (acertou):
            print ("\nVocê acertou!! Ganhou {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("\nVocê errou, tente um numero maior")
            elif (menor):
                print("\nVocê errou, tente um numero menor")
            pontosperdidos = abs(numsecreto - int(chute))
            pontos -= pontosperdidos
        
        if (errou):
            print ("\nVocê errou. O número era: ", numsecreto)

    print("\n*******************")
    print("    Fim do jogo      ")
    print("*******************")

if(__name__ == "__main__"):
    jogar()

#*******
# ---------------- ou ------------------
# chute_str = input("Digite o seu número: ")
# chute = int(chute_str)

# print("Você digitou: ", chute)