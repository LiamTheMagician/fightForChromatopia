import pygame
import time as framerate
import sys
from level import *
from menu import *
from menu_items import *

screen    = pygame.display.set_mode((720,480))

game_run = False
menu_run = True

main_menu_buttons = [
    Button('Play', text_color=(255,255,255), font_size= 30,position=(720/2, 480/2), size=(200, 50))
]

class Game():
    def __init__(self, level_path, player_speed):
        pygame.init()
        
        self.player_speed = player_speed
        self.level = Level(level_path)
        self.level.tile_mapping(self.player_speed)

        self.prev_time = framerate.time()
        self.i = 1

    def change_level(self, level_path):
        self.level = Level(level_path)
        self.level.tile_mapping(self.player_speed)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def check_status(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return False
        return True
    
    def change_status(self):
        ...

    def fps(self, dt):
        self.i -= 1*dt
        if self.i <= 0:
            print(1/dt)
            self.i = 0.5

    def run_game(self):
        dt = framerate.time() - self.prev_time
        self.prev_time = framerate.time()

        screen.fill((67, 171, 230))

        self.check_events()
        self.fps(dt)
        self.level.level_run(dt)

        pygame.display.flip()

main_game = Game("map/map1.csv", 400)
main_menu = Menu("art/wallpaper.png", main_menu_buttons)

running = True
while running:
    if game_run and menu_run == False:
        main_game.run_game()

        game_run = main_game.check_status()
        menu_run = not main_game.check_status() #not inverses le bool

    if menu_run and game_run == False:
        main_menu.run_menu()

        if main_menu.get_button(0) and game_run == False:
            menu_run = False
            game_run = True
            
    if not game_run and not menu_run:
        pygame.quit()
        sys.exit()