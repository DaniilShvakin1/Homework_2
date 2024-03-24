import pygame
import time


choose = int(input("Выберите персонажа:\n1)шрек (базовый)\n2)осел\n>>>"))

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('2D Plaformer')

# загрузка персонажа и монетки
if choose == 1:
    character = pygame.image.load('1666265817_39-mykaleidoscope-ru-p-shrek-chelovek-vkontakte-43 (1).jpg')
elif choose == 2:
    character = pygame.image.load('img/osel.png')
else:
    raise ValueError('Такого персонажа нет')

coin = pygame.image.load('4b809286882144f289d5b04c4d22e140.jpeg')
background = pygame.image.load('i-125-13.jpeg')

# настройка начальных координат
if choose == 1:
    x = 400
    y = 300
    direction = 'right'
elif choose == 2:
    x = 100
    y = 100
    direction = 'left'

vx = 0
vy = 0

# координаты монет
coins = [(600, 200), (300, 400), (500, 300), (700, 100)]

# счет
score = 0

# контроль частоты кадров
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    events = pygame.event.get()

    # работа с событиями
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if choose == 1:
                    vx = -5
                elif choose == 2:
                    vx = -20
                direction = 'left'

            if event.key == pygame.K_RIGHT:
                if choose == 1:
                    vx = 5
                elif choose == 2:
                    vx = 20
                direction = 'right'

            if event.key == pygame.K_UP:
                if choose == 1:
                    vy = -10
                elif choose == 2:
                    vy = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vx = 0

    # обновление координат с учетом скорости и гравитации
    x += vx
    y += vy
    vy += 1

    # ограничения на выход за границы карты
    if x < 0:
        if choose == 1:
            x = 0
        elif choose == 2:
            x = 10
    if x > 800:
        if choose == 1:
            x = 800
        elif choose == 2:
            x = 600
    if y < 0:
        if choose == 1:
            y = 200
        elif choose == 2:
            y = 550
    # пол
    if y > 600:
        y = 550

    screen.blit(background, (0, 0))

    # отобразил персонажа
    if direction == 'right':
        screen.blit(character, (x, y))
    else:
        flipped = pygame.transform.flip(character, True, False)
        screen.blit(flipped, (x, y))

    # отобразил монеты
    for coord in coins:
        screen.blit(coin, (coord[0], coord[1]))

    for i, (cx, cy) in enumerate(coins):
        if ((x + 25) - (cx + 25)) ** 2 + ((y + 25) - (cy + 25)) ** 2 < 50 ** 2:
            score += 1
            del coins[i]

    font = pygame.font.SysFont('Arial', 32)
    text = font.render(f"Счет {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # обновление экрана
    pygame.display.flip()