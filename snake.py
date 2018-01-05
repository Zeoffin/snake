import pygame
import random

pygame.init()

font_size = 50
font = pygame.font.SysFont(None, font_size)


# Functions


def message(width, height, msg, color):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [width, height])


def snake(snakeList):

    for position in snakeList:
        pygame.draw.rect(display, red, [position[0], position[1], 10, 10])


# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 102, 0)
gray = (192, 192, 192)

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()


# Game loop
def gameLoop():

    gameExit = False
    gameOver = False

    score = 0

    # Snake
    lead_x = random.randrange(1, 790)
    lead_y = random.randrange(1, 590)
    lead_x_change = 0
    lead_y_change = 0
    snake_speed = 70
    snakeList = []
    snakeLength = 1

    # Food
    food_x = random.randrange(1, 790)
    food_y = random.randrange(1, 590)

    while not gameExit:

        # Losing
        while gameOver == True:
            display.fill(gray)
            message(display_width/8, (display_height/2) - 50, "SPACE - play again      ESC - quit", black)
            message(display_width / 3, (display_height / 2) + 50, "Your score: {}".format(score), black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False

                    elif event.key == pygame.K_SPACE:
                        gameLoop()

                elif event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

        # Event handling
        for event in pygame.event.get():

            # Exit game
            if event.type == pygame.QUIT:
                gameExit = True

            # Move (key down)
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    lead_x_change = -2
                    lead_y_change = 0

                elif event.key == pygame.K_d:
                    lead_x_change = 2
                    lead_y_change = 0

                elif event.key == pygame.K_w:
                    lead_y_change = -2
                    lead_x_change = 0

                elif event.key == pygame.K_s:
                    lead_y_change = 2
                    lead_x_change = 0

                # Exit game
                elif event.key == pygame.K_ESCAPE:
                    gameExit = True
                    gameOver = False

        lead_x += lead_x_change
        lead_y += lead_y_change

        # Background
        display.fill(gray)

        # Snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        snake(snakeList)

        # Food
        pygame.draw.rect(display, green, [food_x, food_y, 10, 10])

        # Eat
        if ((food_x+10) >= lead_x >= (food_x-10)) and ((food_y+10) >= lead_y >= (food_y-10)):

            food_x = random.randrange(1, 790)
            food_y = random.randrange(1, 590)
            snake_speed += 5
            snakeLength += 10
            score += 1

        # Lose EDGES
        if lead_x > 790 or lead_x < 0 or lead_y > 590 or lead_y < 0:
            gameOver = True

        # Lose INTO YOURSELF
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()