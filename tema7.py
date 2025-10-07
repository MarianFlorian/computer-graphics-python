import pygame, sys, random, os

# Setup
pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Culori
WHITE, RED, GREEN = (255,255,255), (255,0,0), (0,255,0)

# Scor
SCORE_FILE = "score.txt"
if not os.path.exists(SCORE_FILE): open(SCORE_FILE, "w").write("0")
with open(SCORE_FILE) as f: high_score = int(f.read())
score = 0

# Grupe
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
bunker_group = pygame.sprite.Group()

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(midbottom=(W//2, H-30))
        self.cooldown = 0

    def update(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0: self.rect.x -= 5
        if keys[pygame.K_d] and self.rect.right < W: self.rect.x += 5
        if keys[pygame.K_SPACE] and self.cooldown == 0:
            player_bullets.add(Bullet(self.rect.centerx, self.rect.top, -6, GREEN))
            self.cooldown = 20
        self.cooldown = max(0, self.cooldown - 1)

# Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dy, color):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.dy = dy
    def update(self):
        self.rect.y += self.dy
        if self.rect.bottom < 0 or self.rect.top > H: self.kill()

# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))

# Bunker
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))

# Init
player = Player()
player_group.add(player)

for row in range(5):
    for col in range(10):
        enemy = Enemy(100 + col*50, 50 + row*30)
        enemy_group.add(enemy)

for bx in [200, 400, 600]:
    for i in range(5):
        for j in range(3):
            bunker_group.add(Block(bx+i*10, H-100+j*10))

 
dx = 2
while True:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            with open(SCORE_FILE, "w") as f: f.write(str(max(score, high_score)))
            pygame.quit(); sys.exit()


    player_group.update(keys)
    player_bullets.update()
    enemy_bullets.update()


    move_down = False
    for enemy in enemy_group:
        enemy.rect.x += dx
        if enemy.rect.right >= W or enemy.rect.left <= 0: move_down = True
    if move_down:
        dx *= -1
        for enemy in enemy_group:
            enemy.rect.y += 10


    cols = {}
    for e in sorted(enemy_group, key=lambda e: e.rect.y, reverse=True):
        col = e.rect.x // 50
        if col not in cols:
            if random.random() < 0.01:
                enemy_bullets.add(Bullet(e.rect.centerx, e.rect.bottom, 4, RED))
            cols[col] = True


    for b in player_bullets:
        hit = pygame.sprite.spritecollide(b, enemy_group, True)
        if hit: b.kill(); score += 10
    pygame.sprite.groupcollide(player_bullets, bunker_group, True, True)
    pygame.sprite.groupcollide(enemy_bullets, bunker_group, True, True)


    def end_game(message):
        screen.fill((0, 0, 0))
        end_text = font.render(message, True, WHITE)
        screen.blit(end_text, (W // 2 - end_text.get_width() // 2, H // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        with open(SCORE_FILE, "w") as f: f.write(str(max(score, high_score)))
        pygame.quit()
        sys.exit()


    # Când ești lovit
    if pygame.sprite.spritecollide(player, enemy_bullets, True):
        end_game("GAME OVER!")

    # Când câștigi
    if len(enemy_group) == 0:
        end_game("YOU WIN!")

    # Draw
    player_group.draw(screen)
    enemy_group.draw(screen)
    player_bullets.draw(screen)
    enemy_bullets.draw(screen)
    bunker_group.draw(screen)

    # Scor
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"High Score: {max(score, high_score)}", True, WHITE), (W-180, 10))

    pygame.display.flip()
    clock.tick(60)
d