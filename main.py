import sys

import pygame as pg
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from snake import Snake

def run_game():

    # Initialize game and create a screen object
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Py Eating Snake")

    # Creating the snake object
    snake = Snake(settings, screen)

    # Start main loop of game.
    while True:

        # setting frame rate
        clock = pg.time.Clock()
        clock.tick_busy_loop(30)

        # Watch for keyboard and mouse events.
        gf.check_event(settings, screen, snake)
        gf.update_screen(settings, screen, snake)


#Staring Game
run_game()
