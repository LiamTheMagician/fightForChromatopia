import pygame

class UI():
    def __init__(self, button_list = []):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.get_surface()

        self.button_list   = button_list
        self.g_buttons   = pygame.sprite.Group(self.button_list)

        self.prev_time = framerate.time()

    def get_button(self, button_index):
        if self.g_buttons.sprites()[button_index].get_clicked():
            return True
        return False

    def run_menu(self):
        dt = framerate.time() - self.prev_time
        self.prev_time = framerate.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        self.g_buttons.update(dt)       
        self.g_wallpaper.draw(self.screen)

        pygame.display.flip()