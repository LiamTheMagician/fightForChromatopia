import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))

player_surf = pygame.image.load('art/player.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (200, 200))

block_surf = pygame.Surface((50,50))

clock = pygame.time.Clock()

def AABB(a, b):
    if ((b.right > a.right > b.left) and (b.left < a.left < b.right)) or ((b.bottom > a.bottom > b.top) and (b.top < a.top < b.bottom)):
        return True
while True:
    screen.fill((50,50,50))
    block_rect = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((1280-100)/2, (720-100)/2, 100, 100))
    screen.blit(player_surf, player_rect)
    print(AABB(player_rect, block_rect))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.y -= 4
    if keys[pygame.K_DOWN]:
        player_rect.y += 4
    if keys[pygame.K_LEFT]:
        player_rect.x -= 4
    if keys[pygame.K_RIGHT]:
        player_rect.x += 4

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(60)