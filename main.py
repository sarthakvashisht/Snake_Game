# importing modules
import pygame
import random
# pygame initialise
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
# variables used
direction = 1
update_snake = 0
Nfood = True
food = [0, 0]
font = pygame.font.SysFont("freeSans.ttf", 38)
score = 0
game_over = False
clicked = False


# game functions
def scores():
    stxt = 'Score:' + str(score)
    simg = font.render(stxt, True, (250, 250, 255))
    screen.blit(simg, (0, 0))


def checkgameover(game_over):
    headcount = 0
    for segment in snake_pos:
        if snake_pos[0] == segment and headcount > 0:  # checking for boundary and lining
            game_over = True
        headcount += 1
    if snake_pos[0][0] < 0 or snake_pos[0][0] > 499 or snake_pos[0][1] < 0 or snake_pos[0][1] > 499:
        game_over = True
    return game_over


def gotxt():
    overtxt = "GAMEOVER"
    overimg = font.render(overtxt, True, (0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (190, 190, 130, 30))
    againtxt = "play again"
    againimg = font.render(againtxt, True, (0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (175, 250, 160, 50))
    screen.blit(againimg, (190, 190))
    screen.blit(overimg, (177, 260))


# creating snake via list
snake_pos = [[int(250), int(250)]]
snake_pos.append([int(250), int(250) + 10])
snake_pos.append([int(250), int(250) + 20])
snake_pos.append([int(250), int(250) + 30])
# game loop
run = True
while run:
    screen.fill((0, 0, 0))  # screen colour
    scores()  # calling score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            # movements
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4
    # checking gameover and updating snake with increasing length by unit size i.e. 10px
    if game_over == False:
        if update_snake > 99:
            update_snake = 0
            snake_pos = snake_pos[-1:] + snake_pos[:-1]
            if direction == 1:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] - 10
            if direction == 3:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] + 10
            if direction == 2:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] + 10
            if direction == 4:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] - 10
            game_over = checkgameover(game_over)
    # creating food
    if Nfood == True:
        Nfood = False
        food[0] = 10 * random.randint(0, 40)
        food[1] = 10 * random.randint(0, 40)
    pygame.draw.rect(screen, (250, 250, 250), (food[0], food[1], 10, 10))
    # iff food eaten increment length by 10px size
    if snake_pos[0] == food:
        Nfood = True
        score += 10
        # increasing length at end of the snake
        Npiece = list(snake_pos[-1])
        if direction == 1:
            Npiece[1] += 10
        if direction == 3:
            Npiece[1] -= 10
        if direction == 4:
            Npiece[0] += 10
        if direction == 2:
            Npiece[0] -= 10
        snake_pos.append(Npiece)
    if game_over == True:
        gotxt()  # calling gameover function
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()  # getting mouse position
            if pygame.draw.rect(screen, (255, 255, 255), (190, 200, 160, 50)).collidepoint(pos):
                # again initialising variables for new snake after play again
                direction = 1
                update_snake = 0
                Nfood = True
                food = [0, 0]
                font = pygame.font.SysFont("freeSans.ttf", 38)
                score = 0
                game_over = False
                snake_pos = [[int(250), int(250)]]
                snake_pos.append([int(250), int(250) + 10])
                snake_pos.append([int(250), int(250) + 20])
                snake_pos.append([int(250), int(250) + 30])
    # differentiating head and body of snake
    head = 1
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen, (255, 255, 255), (x[0], x[1], 10, 10))
            pygame.draw.rect(screen, (255, 255, 255), (x[0] + 1, x[1] + 1, 8, 8))
        if head == 1:
            pygame.draw.rect(screen, (255, 255, 255), (x[0], x[1], 10, 10))
            pygame.draw.rect(screen, (0, 0, 0), (x[0] + 1, x[1] + 1, 8, 8))
            head = 0
    pygame.display.update()
    update_snake += 0.5
pygame.quit()
