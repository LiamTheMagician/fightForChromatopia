import pygame
import time as framerate
from level import *
from menu import *
from menu_items import *

screen = pygame.display.set_mode((720,480))

game_run = False
menu_run = True

main_menu_buttons = [
    Button(position=(720/2, 480/2), size=(200, 50))
]

class Game():
    def __init__(self):
        pygame.init()
        self.prev_time = framerate.time()

        self.level = Level("map/map1.csv")
        self.level.tile_mapping(300)

    def run_game(self):
        dt = framerate.time() - self.prev_time
        self.prev_time = framerate.time()

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill((50,50,50))

        self.level.level_run(dt)
        pygame.display.flip()

main_game = Game()
main_menu = Menu("art/wallpaper.png", main_menu_buttons)

while True:
    print(menu_run)
    if game_run:
        main_game.run_game()
    if menu_run and game_run == False:
        main_menu.run_menu()
        if main_menu.get_button(0) and game_run == False:
            game_run = True
            menu_run = False