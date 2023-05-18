import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Load visual assets
sprite_sheet = pygame.image.load("snake-graphics.png").convert_alpha()

# Scale the sprites
snake_head_img = pygame.transform.scale(sprite_sheet.subsurface(pygame.Rect(192, 0, 64, 64)), (20, 20))
snake_body_img = pygame.transform.scale(sprite_sheet.subsurface(pygame.Rect(0, 0, 64, 64)), (20, 20))
food_img = pygame.transform.scale(sprite_sheet.subsurface(pygame.Rect(128, 0, 64, 64)), (20, 20))
background_img = pygame.transform.scale(pygame.image.load("background.png").convert(), (width, height))

# Set up the Snake
snake_size = 20
snake_speed = 15
x_pos = width // 2
y_pos = height // 2
x_speed = 0
y_speed = 0
snake_body = []
snake_length = 1

# Set up the Food
food_x = round(random.randrange(0, width - snake_size) / 20) * 20
food_y = round(random.randrange(0, height - snake_size) / 20) * 20

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# Game Menu
def game_menu():
    menu_font = pygame.font.Font(None, 48)
    title_text = menu_font.render("Snake Game", True, (255, 255, 255))
    play_text = font.render("Press SPACE to Play", True, (255, 255, 255))
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
    over_font = pygame.font.Font(None, 48)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    menu_text = font.render("Press M for Menu", True, (255, 255, 255))

    window.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() * 2))
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
                elif event.key == pygame.K_m:
                    return False

# Game Loop
def game_loop():
    global x_pos, y_pos, x_speed, y_speed, snake_body, snake_length, food_x, food_y, score

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

        x_pos += x_speed
        y_pos += y_speed

        if x_pos < 0 or x_pos >= width or y_pos < 0 or y_pos >= height:
            game_over = True

        snake_head = []
        snake_head.append(x_pos)
        snake_head.append(y_pos)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        if x_pos == food_x and y_pos == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 20) * 20
            food_y = round(random.randrange(0, height - snake_size) / 20) * 20
            snake_length += 1
            score += 1

        window.blit(sprite_sheet, (x_pos, y_pos), pygame.Rect(192, 0, 64, 64))  # Draw snake head
        for segment in snake_body[1:]:
            window.blit(sprite_sheet, (segment[0], segment[1]), pygame.Rect(0, 0, 64, 64))  # Draw snake body
        window.blit(sprite_sheet, (food_x, food_y), pygame.Rect(128, 0, 64, 64))  # Draw food

        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        window.blit(score_text, (10, 10))

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
