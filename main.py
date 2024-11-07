import pygame
import random

#configs
pygame.init()
pygame.display.set_caption("Snake Game")
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


#cores 
co_black = (0, 0, 0)
co_white = (255, 255, 255)
co_Lgreen = (144,238,144)
co_green = (0, 255, 0)



# parametros da cobra
container = 20
speed_game = 15


#função do game
def generate_food():
    food_x = round(random.randrange(0, width - container) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - container) / 20.0) * 20.0
    return food_x, food_y


def draw_food(container_food, food_x, food_y):
    pygame.draw.rect(screen, co_green, [food_x, food_y, container_food, container_food])

def draw_snake(container_snake, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, co_Lgreen, [pixel[0], pixel[1], container_snake, container_snake])

def draw_points(point):
    font = pygame.font.SysFont('Arial', 25)
    text = font.render(f"Pontos: {point}", True, co_white)
    screen.blit(text, [2, 1])

def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = container
    elif key == pygame.K_UP:
        speed_x = 0
        speed_y = -container
    elif key == pygame.K_RIGHT:
        speed_x = container
        speed_y = 0
    elif key == pygame.K_LEFT:
        speed_x = -container
        speed_y = 0

    return speed_x, speed_y

def game():
    end_game = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    size_snake = 1
    pixels = []

    food_x, food_y = generate_food()
     



    while not end_game:
        screen.fill(co_black)

        #evento do game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)


        #Desenho da comida
        draw_food(container, food_x, food_y)

        #Atualização da Cobra
        if x < 0 or x >= width or y < 0 or y >=height:
            end_game = True

        x += speed_x
        y += speed_y

        # Logica da Cobra
        pixels.append([x, y])
        if len(pixels) >  size_snake:
               del pixels[0]

        # Caso a cobra bata no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                end_game = True

        #Desenho da cobra
        draw_snake(container, pixels)

        #Desenho pontuação
        draw_points(size_snake - 1)
    
    
        # Att jogo
        pygame.display.update()

        # Criando nova comida
        if x == food_x and y == food_y:
            size_snake += 1
            food_x, food_y = generate_food()

        clock.tick(speed_game)

game()