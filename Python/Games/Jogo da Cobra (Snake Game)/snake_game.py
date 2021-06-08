import turtle
import time
import random

delay = 0.1  # Delay (Atraso)

# Placares
score = 0
high_score = 0

# Janela
wn = turtle.Screen()  # Inicilaizar tela
wn.title("Jogo da cobra")  # Nome
wn.bgcolor("green")  # Cor de fundo
wn.setup(width=600, height=600)  # Tamanho
wn.tracer(0)  # Desliga a atualizaçção da tela

# Cabeça da cobra
head = turtle.Turtle()
head.speed(0)  # Velocidade
head.shape("square")  # Formato
head.color("black")  # Cor
head.goto(0, 0)  # Lugar na tela
head.penup()  # Retira tracejado
head.direction = "stop"  # Direção

# Maçã da Cobra
apple = turtle.Turtle()
apple.speed(0)  # Velocidade
apple.shape("circle")  # Formato
apple.color("red")  # Cor
apple.penup()  # Retira tracejado
apple.goto(0, 100)  # Lugar na tela

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)  # Velocidade
pen.shape("square")  # Formato
pen.color("white")  # Cor
pen.penup()  # Retira tracejado
pen.hideturtle()  # Esconder
pen.goto(0, 260)  # Lugar da tela
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))  # Escrever


# Funções
# Mudar de direção e Movimento
def move():
    if head.direction == "up":  # Movimento para cima
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":  # Movimento para baixo
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":  # Movimento para esquerda
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":  # Movimento para direita
        x = head.xcor()
        head.setx(x + 20)


def go_up():  # Cima
    if head.direction != "down":
        head.direction = "up"


def go_down():  # Baixo
    if head.direction != "up":
        head.direction = "down"


# Esquerda
def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():  # Direita
    if head.direction != "left":
        head.direction = "right"


# Controle no teclado
wn.listen()
wn.onkeypress(go_up, "Up")  # Seta para Cima
wn.onkeypress(go_down, "Down")  # Seta para Baixo
wn.onkeypress(go_left, "Left")  # Seta para Esquerda
wn.onkeypress(go_right, "Right")  # Seta para Direita

# Loop do Jogo
while True:
    wn.update()  # Atualizando a o jogo

    # Verifica colisão com a borda
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # Delay
        head.goto(0, 0)  # Resetar o local do jogador
        head.direction = "stop"  # Parar

        # Esconder seguimentos
        for segment in segments:
            segment.goto(1000, 1000)

        # Limpa lista de seguimentos
        segments.clear()

        # Resetar placa
        score = 0

        # Resetar delay
        delay = 0.1

        # Atualizar placar
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Verifica colisão com a maçã
    if head.distance(apple) < 20:
        # Move a maçã para um lugar aleatorio
        x = random.randint(-290, 290)  # Cordenada x
        y = random.randint(-290, 290)  # Cordenada y
        apple.goto(x, y)  # Lugar na tela, com as variaveis aleatórias

        # Adiciona seguimento da cobra
        new_segment = turtle.Turtle()
        new_segment.speed(0)  # Velocidade
        new_segment.shape("square")  # Formato
        new_segment.color("grey")  # Cor
        new_segment.penup()  # Retira tracejado
        segments.append(new_segment)  # Adicionar seguimento

        # Encurta delay
        delay -= 0.001

        # Aumentar o placar
        score += 1

        # Se o placar for melhor do que o melhor placar substitua
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move segmentos finais primeiro em ordem reversa
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)  # Local

    # Mover seguimento 0 para a cabeça estar
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)  # Local

    move()  # Função de movimento

    # Verificar colisão com corpo
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)  # Delay
            head.goto(0, 0)  # Resertar local do jogador
            head.direction = "stop"  # Parar

            # Esconder os seguimentos
            for segment in segments:
                segment.goto(1000, 1000)

            # Limpa lista de seguimentos
            segments.clear()

            # Resetar placar
            score = 0

            # Atualizar placar
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
