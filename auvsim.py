
import pygame
import sys
import random


WIDTH, HEIGHT = 800, 600


auv_radius = 20  
auv_color = (0, 0, 255)  
auv_speed = 10 


sea_color = (0, 0, 128)  


auv_x = WIDTH // 2
auv_y = HEIGHT // 2

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("AUV Simülasyonu")


clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and auv_x - auv_speed > 0:
        auv_x -= auv_speed
    if keys[pygame.K_RIGHT] and auv_x + auv_speed < WIDTH:
        auv_x += auv_speed
    if keys[pygame.K_UP] and auv_y - auv_speed > 0:
        auv_y -= auv_speed
    if keys[pygame.K_DOWN] and auv_y + auv_speed < HEIGHT:
        auv_y += auv_speed

   
    screen.fill(sea_color)


    pygame.draw.circle(screen, auv_color, (auv_x, auv_y), auv_radius)

    pygame.display.flip()

  
    clock.tick(20)