import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
GRAY = (200, 200, 200)
RED = (255, 50, 50)

def draw_snowman(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 30)      # cap
    pygame.draw.circle(screen, WHITE, (x, y + 45), 40) # mijloc
    pygame.draw.circle(screen, WHITE, (x, y + 100), 50)# bază
    pygame.draw.circle(screen, BLACK, (x - 10, y - 10), 4) # ochi stâng
    pygame.draw.circle(screen, BLACK, (x + 10, y - 10), 4) # ochi drept

# Desen fulg de nea rotitor
def draw_rotating_snowflake(center, angle):
    x, y = center
    r = 20
    for i in range(6):
        rad = math.radians(i * 60 + angle)
        x_end = x + r * math.cos(rad)
        y_end = y + r * math.sin(rad)
        pygame.draw.line(screen, BLUE, (x, y), (x_end, y_end), 2)

# Desen avion
def draw_plane(x, y):
    pygame.draw.polygon(screen, RED, [(x, y), (x - 40, y + 10), (x - 40, y - 10)])


plane_x = 0
plane_y = 100
angle = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GRAY)


    draw_snowman(200, 350)
    draw_snowman(600, 350)


    draw_rotating_snowflake((400, 150), angle)
    angle += 2


    draw_plane(plane_x, plane_y)
    plane_x += 3
    if plane_x > WIDTH + 50:
        plane_x = -50

    pygame.display.flip()
    clock.tick(60)
