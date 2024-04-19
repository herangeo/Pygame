import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Multiple Images Example")

background_image = pygame.image.load("whiteback.png")

jet_image = pygame.image.load("jet3.jpg")
jet_image = pygame.transform.scale(jet_image, (200, 200))

bomb_image = pygame.image.load("bomb.jpg")
bomb_image = pygame.transform.scale(bomb_image, (50, 50))

house_image = pygame.image.load("house.jpg")
explode_image = pygame.image.load("explode.jpg")
explode_image = pygame.transform.scale(explode_image, (100, 100))

jet_x = 0
jet_y = 0
jet_speed = 5

bomb_x = random.randint(0, screen_width - bomb_image.get_width())
bomb_y = -bomb_image.get_height()
bomb_speed = 5
bomb_falling = False

house_x = 300
house_y = 400
house_width = house_image.get_width()
house_height = house_image.get_height()
house_visible = True
explosion_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    jet_x += jet_speed

    if jet_x > screen_width / 2 and not bomb_falling:
        bomb_falling = True

    if bomb_falling:
        bomb_y += bomb_speed
        if bomb_y > screen_height:
            bomb_x = random.randint(0, screen_width - bomb_image.get_width())
            bomb_y = -bomb_image.get_height()
            bomb_falling = False

        # Collision detection
        bomb_rect = pygame.Rect(bomb_x, bomb_y, bomb_image.get_width(), bomb_image.get_height())
        house_rect = pygame.Rect(house_x, house_y, house_width, house_height)
        if bomb_rect.colliderect(house_rect) and house_visible:
            house_visible = False
            explosion_time = pygame.time.get_ticks()

    if jet_x > screen_width:
        jet_x = 0

    screen.fill((255, 255, 255))

    screen.blit(background_image, (0, 0))

    screen.blit(jet_image, (jet_x, jet_y))

    if house_visible:
        screen.blit(house_image, (house_x, house_y))
    
    if bomb_falling:
        screen.blit(bomb_image, (bomb_x, bomb_y))

    if not house_visible and pygame.time.get_ticks() - explosion_time < 1000:
        screen.blit(explode_image, (house_x - 25, house_y - 25))

    pygame.display.flip()

    pygame.time.delay(30)  # Delay to control animation speed

pygame.quit()
sys.exit()
