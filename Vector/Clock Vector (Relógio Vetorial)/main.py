import pygame
import time

pygame.init()

# Time
clock = pygame.time.Clock()
realSeconds = 0
realMinutes = 0
realHours = 0
seconds = 250
minutes = 250
hours = 250

# Color (Cor)
white = [255, 255, 255]
black = [0, 0, 0]

# Window (Janela)
size = widthScreen, heigthScreen = 500, 500  # Size (Tamanho)
screen = pygame.display.set_mode(size)

running = True


def number_one(xPos, yPos):
    pygame.draw.line(screen, white, (xPos + 230, yPos + 20), (xPos + 220, yPos + 25))
    pygame.draw.line(screen, white, (xPos + 230, yPos + 20), (xPos + 230, yPos + 60))


def pointer_second(second):
    pygame.draw.line(screen, white, (250, 250), (second, 20), 2)


def pointer_minute(minute):
    pygame.draw.line(screen, white, (250, 250), (minute, 50), 5)


def pointer_hour(hour):
    pygame.draw.line(screen, white, (250, 250), (hour, 100), 5)


while running:
    clock.tick(1)
    title = time.strftime("%H:%M:%S - Vector Clock", time.localtime())
    pygame.display.set_caption(title)
    realSeconds = time.strftime("%S", time.localtime())
    realSeconds = int(realSeconds)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                seconds += 1

        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    pygame.draw.circle(screen, white, (250, 250), 240, 1)
    number_one(0, 0)
    number_one(100, 20)
    number_one(-80, 25)
    pointer_second(realSeconds)
    pointer_minute(minutes)
    pointer_hour(hours)
    pygame.display.update()
