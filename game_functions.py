import sys

import pygame as pg
from snake import Snake

def update_screen(settings,screen,snake):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(settings.bg_color)

    #draw snake to screen
    snake.draw()

    # Make the most recently drawn screen visible
    pg.display.flip()

def check_event(settings, screen, snake):
    """Respond to keypresses and mouse events """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event,settings, screen, snake)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, snake)

def check_keydown_events(event,settings,screen,snake):
    """ Respond to keypresses """
    if event.key == pg.K_d:
        print('d')
    elif event.key == pg.K_a:
        print('a')
    elif event.key == pg.K_w:
        print('w')
    elif event.key == pg.K_s:
        print('s')

def check_keyup_events(event,snake):
    if event.key == pg.K_d:
        print('d')
    elif event.key == pg.K_a:
        print('a')
    elif event.key == pg.K_w:
        print('w')
    elif event.key == pg.K_s:
        print('s')
