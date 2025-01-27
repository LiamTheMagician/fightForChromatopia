import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))

player_surf = pygame.image.load('art/player.png').convert_alpha()
player_rect = player_surf.get_rect()

clock = pygame.time.Clock()

while True:
    screen.fill((50,50,50))
    screen.blit(player_surf, player_rect)

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

    
