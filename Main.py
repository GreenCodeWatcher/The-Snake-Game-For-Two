import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
NICE_GRAY = (50, 50, 50)

#graphics
background_img = pygame.image.load("background.png").convert()
logo_img = pygame.image.load("snake_head.png").convert()
logo_img.set_colorkey(BLACK)
background_img = pygame.transform.smoothscale(background_img, window.get_size())
strawberry_img = pygame.image.load("strawberry.png").convert()
strawberry_img = pygame.transform.smoothscale(strawberry_img,(20, 20))
strawberry_img.set_colorkey(BLACK)
apple_img = pygame.image.load("apple.png").convert()
apple_img = pygame.transform.smoothscale(apple_img,(20, 20))
apple_img.set_colorkey(BLACK)

snake_head_img = pygame.image.load("snake_head.png").convert()
snake_head_img = pygame.transform.smoothscale(snake_head_img,(40, 40))
snake_head_img.set_colorkey(BLACK)


# Set up the Snake
snake_size = 20
snake_speed = 15
x_pos = width // 2
y_pos = height // 2
x_speed = 0
y_speed = 0
snake_body = []
snake_length = 1

# Set up the Snake2
snake1_size = 20
snake1_speed = 15
x1_pos = width // 2
y1_pos = height // 2
x1_speed = 0
y1_speed = 0
snake1_body = []
snake1_length = 1

# Set up the Food
food_x = round(random.randrange(0, width - snake_size) / 20) * 20
food_y = round(random.randrange(0, height - snake_size) / 20) * 20

food1_x = round(random.randrange(0, width - snake1_size) / 20) * 20
food1_y = round(random.randrange(0, height - snake1_size) / 20) * 20

score = 0
score1 = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# Game Menu
def game_menu():
    window.fill(BLACK)
    window.blit(background_img, (0, 0))
    window.blit(logo_img, (150, -75))
    menu_font = pygame.font.Font(None, 48)
    title_text = menu_font.render("Snake Game", True, WHITE)
    play_text = font.render("Press SPACE to Play", True, WHITE)
    window.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - title_text.get_height()))
    window.blit(play_text, (width // 2 - play_text.get_width() // 2, height // 2 + play_text.get_height()))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

# Game Over Screen
def game_over_screen():
    window.fill(NICE_GRAY)
    over_font = pygame.font.Font(None, 48)
    score_text = font.render("Score: " + str(score), True, GREEN)
    score1_text = font.render("Score: " + str(score1), True, WHITE)
    over_text = over_font.render("Game Over", True, WHITE)
    restart_text = font.render("Press R to Restart", True, WHITE)
    menu_text = font.render("Press ESC for Exit", True, RED)
    window.blit(score_text, (width // 2 - score_text.get_width()// 2, height // 2 - score_text.get_height() * 2 - 30))
    window.blit(score1_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() * 2 - 10))
    window.blit(over_text, (width // 2 - over_text.get_width() // 2, height // 2 - over_text.get_height()))
    window.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2))
    window.blit(menu_text, (width // 2 - menu_text.get_width() // 2, height // 2 + menu_text.get_height()))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

# Game Loop
def game_loop():
    global x_pos, y_pos, x_speed, y_speed, snake_body, snake_length, food_x, food_y, score, x1_pos, y1_pos, x1_speed, y1_speed, snake1_body, snake1_length, score1, food1_x, food1_y

    # Reset the game variables
    x_pos = width // 2
    y_pos = height // 2
    x_speed = 0
    y_speed = 0
    snake_body = []
    snake_length = 1
    food_x = round(random.randrange(0, width - snake_size) / 20) * 20
    food_y = round(random.randrange(0, height - snake_size) / 20) * 20
    score = 0

    x1_pos = width // 2 + snake1_size
    y1_pos = height // 2 + snake1_size
    x1_speed = 0
    y1_speed = 0
    snake1_body = []
    snake1_length = 1
    food1_x = round(random.randrange(0, width - snake_size) / 20) * 20
    food1_y = round(random.randrange(0, height - snake_size) / 20) * 20
    score1 = 0

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and y_speed != snake_size:
                    x_speed = 0
                    y_speed = -snake_size
                elif event.key == pygame.K_DOWN and y_speed != -snake_size:
                    x_speed = 0
                    y_speed = snake_size
                elif event.key == pygame.K_LEFT and x_speed != snake_size:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT and x_speed != -snake_size:
                    x_speed = snake_size
                    y_speed = 0
                    window.blit(snake_head_img, (x_pos-10, y_pos-10))
                elif event.key == pygame.K_w and y1_speed != snake1_size:
                    x1_speed = 0
                    y1_speed = -snake1_size
                elif event.key == pygame.K_s and y1_speed != -snake1_size:
                    x1_speed = 0
                    y1_speed = snake1_size
                elif event.key == pygame.K_a and x1_speed != snake1_size:
                    x1_speed = -snake1_size
                    y1_speed = 0
                elif event.key == pygame.K_d and x1_speed != -snake_size:
                    x1_speed = snake1_size
                    y1_speed = 0

        x_pos += x_speed
        y_pos += y_speed
        x1_pos += x1_speed
        y1_pos += y1_speed

        #Eating
        if x_pos == food_x and y_pos == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 20) * 20
            food_y = round(random.randrange(0, height - snake_size) / 20) * 20
            snake_length += 1
            score += 1

        if x_pos == food1_x and y_pos == food1_y:
            food1_x = round(random.randrange(0, width - snake_size) / 20) * 20
            food1_y = round(random.randrange(0, height - snake_size) / 20) * 20
            snake1_length = snake1_length -1
            score1 -= 1

        if x1_pos == food_x and y1_pos == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 20) * 20
            food_y = round(random.randrange(0, height - snake_size) / 20) * 20
            snake_length = snake_length-1 
            score -= 1

        if x1_pos == food1_x and y1_pos == food1_y:
            food1_x = round(random.randrange(0, width - snake1_size) / 20) * 20
            food1_y = round(random.randrange(0, height - snake1_size) / 20) * 20
            snake1_length += 1
            score1 += 1

        #Gameover
        if x_pos < 0 or x_pos >= width or y_pos < 0 or y_pos >= height or x1_pos < 0 or x1_pos >= width or y1_pos < 0 or y1_pos >= height:
            game_over = True

        snake_head = []
        snake_head.append(x_pos)
        snake_head.append(y_pos)
        snake_body.append(snake_head)

        snake1_head = []
        snake1_head.append(x1_pos)
        snake1_head.append(y1_pos)
        snake1_body.append(snake1_head)

        if len(snake_body) > snake_length:
            del snake_body[0]
        if len(snake1_body) > snake1_length:
            del snake1_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True
        
        for segment in snake1_body[:-1]:
            if segment == snake1_head:
                game_over = True

        for segment in snake_body[:-1]:
            if segment == snake1_head:
                game_over = True

        for segment in snake1_body[:-1]:
            if segment == snake_head:
                game_over = True

      
#####################
        window.fill(NICE_GRAY)
        
        for segment in snake_body:
            pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], snake_size, snake_size))
        for segment in snake1_body:
            pygame.draw.rect(window, WHITE, pygame.Rect(segment[0], segment[1], snake1_size, snake1_size))

        window.blit(strawberry_img, (food_x, food_y))
        window.blit(apple_img, (food1_x, food1_y))


        score_text = font.render("Score: " + str(score), True, GREEN)
        score1_text = font.render("Score: " + str(score1), True, WHITE)
        window.blit(score_text, (10, 10))
        window.blit(score1_text, (10, 30))

        pygame.display.update()
        clock.tick(snake_speed)

# Game Execution
while True:
    game_menu()
    game_loop()
    restart = game_over_screen()
    if not restart:
        break

pygame.quit()
