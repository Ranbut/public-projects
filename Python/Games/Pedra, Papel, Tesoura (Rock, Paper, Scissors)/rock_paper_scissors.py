import random

# Variaveis:
inEnglish = False
running = True
placarJogador = 0
placarMaquina = 0
escolhaJogador = 0  # 1 = Pedra; 2 = Papel; 3 = Tesoura
escolhaMaquina = 0  # 1 = Pedra; 2 = Papel; 3 = Tesoura

print("Pedra, Papel, Tesoura!")
while running:
    if not inEnglish:
        print(" ")
        print("Jogador: ", placarJogador, "     Máquina: ", placarMaquina)
        print(" ")
        print("Escolha usando o teclado do número correspodente a opção:")
        print("1 = Pedra")
        print("2 = Papel")
        print("3 = Tesoura")
        print("0 = Sair do Programa")
        print("5 = Play in English (Jogar em Inglês)")
        print(" ")
        escolhaJogador = int(input("Escolha: "))
        escolhaMaquina = random.randint(1, 3)
        print(" ")
        if escolhaJogador == 0:
            running = False

        elif escolhaJogador == 1:
            print("Você escolheu: Pedra!")
            if escolhaMaquina == 1:
                print("A máquina escolhe: Pedra!")
                print(" ")
                print("Isso é um empate!")
            elif escolhaMaquina == 2:
                print("A máquina escolhe: Papel!")
                print(" ")
                print("Você perdeu!")
                placarMaquina += 1
            elif escolhaMaquina == 3:
                print("A máquina escolhe: Tesoura!")
                print(" ")
                print("Você ganhou!")
                placarJogador += 1

        elif escolhaJogador == 2:
            print("Você escolheu: Papel!")
            if escolhaMaquina == 1:
                print("A máquina escolhe: Pedra!")
                print(" ")
                print("Você ganhou!")
                placarJogador += 1
            elif escolhaMaquina == 2:
                print("A máquina escolhe: Papel!")
                print(" ")
                print("Isso é um empate!")
            elif escolhaMaquina == 3:
                print("A máquina escolhe: Tesoura!")
                print(" ")
                print("Você perdeu!")
                placarMaquina += 1

        elif escolhaJogador == 3:
            print("Você escolheu: Tesoura!")
            if escolhaMaquina == 1:
                print("A máquina escolhe: Pedra!")
                print(" ")
                print("Você perdeu!")
                placarMaquina += 1
            elif escolhaMaquina == 2:
                print("A máquina escolhe: Papel!")
                print(" ")
                print("Você ganhou!")
                placarJogador += 1
            elif escolhaMaquina == 3:
                print("A máquina escolhe: Tesoura!")
                print(" ")
                print("Isso é um empate!")

        elif escolhaJogador == 5:
            print("Switching to English!")
            inEnglish = True

        elif escolhaJogador == 0:
            running = False

        else:
            print("Opção Invalida!")

    if inEnglish is True:
        print(" ")
        print("Player: ", placarJogador, "     Machine: ", placarMaquina)
        print(" ")
        print("Chose using the keyboard of the number of desired option:")
        print("1 = Rock")
        print("2 = Paper")
        print("3 = Scissors")
        print("0 = Exit Program")
        print("5 = Jogar em Português (Play in Portuguese)")
        print(" ")
        escolhaJogador = int(input("Chose: "))
        escolhaMaquina = random.randint(1, 3)
        print(" ")
        if escolhaJogador == 0:
            running = False

        elif escolhaJogador == 1:
            print("You chose: Rock!")
            if escolhaMaquina == 1:
                print("The machine choose: Rock!")
                print(" ")
                print("A draw!")
            elif escolhaMaquina == 2:
                print("The machine choose: Papel!")
                print(" ")
                print("You lose!")
                placarMaquina += 1
            elif escolhaMaquina == 3:
                print("The machine choose: Scissors!")
                print(" ")
                print("You win!")
                placarJogador += 1

        elif escolhaJogador == 2:
            print("You chose: Paper!")
            if escolhaMaquina == 1:
                print("The machine choose: Rock!")
                print(" ")
                print("You win!")
                placarJogador += 1
            elif escolhaMaquina == 2:
                print("The machine choose: Paper!")
                print(" ")
                print("A draw!")
            elif escolhaMaquina == 3:
                print("The machine choose: Scissors!")
                print(" ")
                print("You lose!")
                placarMaquina += 1

        elif escolhaJogador == 3:
            print("You chose: Scissors!")
            if escolhaMaquina == 1:
                print("The machine choose: Rock")
                print(" ")
                print("You lose!")
                placarMaquina += 1
            elif escolhaMaquina == 2:
                print("The machine choose: Paper!")
                print(" ")
                print("You win!")
                placarJogador += 1
            elif escolhaMaquina == 3:
                print("The machine choose: Scissors!")
                print(" ")
                print("A draw!")

        elif escolhaJogador == 5:
            print("Mudando para o Português!")
            inEnglish = False

        elif escolhaJogador == 0:
            running = False

        else:
            print("Invalid Option!")
