import sys

import pygame as pg
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from snake import Snake
from food import Food

def run_game():

    # Initialize game and create a screen object
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Py Eating Snake")

    # Creating the snake object
    snake = Snake(settings, screen)
    food = Food(settings, screen, snake)

    # Start main loop of game.
    while True:

        # setting frame rate
        clock = pg.time.Clock()
        clock.tick_busy_loop(20)

        # Watch for keyboard and mouse events.
        gf.check_event(settings, screen, snake, food)
        gf.update_screen(settings, screen, snake, food)


#Staring Game
run_game()
