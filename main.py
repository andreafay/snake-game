import pygame
import random

# pygame setup
pygame.init()
square_width = 600
pixel_width = 50
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True

pixel_width = 25

def generate_random_pos():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]

def is_out_of_bounds():
    return snake_pixel.bottom > square_width or snake_pixel.top < 0 \
        or snake_pixel.left < 0 or snake_pixel.right > square_width

def reset():
    food.center = generate_random_pos()
    snake_pixel.center = generate_random_pos()
    return snake_pixel.copy()

#Snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
snake_pixel.center = generate_random_pos()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

#Food
food = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
food.center = generate_random_pos()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    if is_out_of_bounds():
        snake_length = 1
        snake_pixel.center = generate_random_pos()
        snake = [snake_pixel.copy()]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_direction = (0, - pixel_width)
    if keys[pygame.K_s]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_a]:
        snake_direction = (- pixel_width, 0)
    if keys[pygame.K_d]:
        snake_direction = (pixel_width, 0)

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)
    
    pygame.draw.rect(screen, "orange", food)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()