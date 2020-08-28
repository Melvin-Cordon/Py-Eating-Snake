import sys
import random

import pygame as pg
from pygame.sprite import Sprite

class Node(Sprite):
    def __init__(self, screen, settings, pos = [250,350], prev_pos = None, next = None, prev = None):
        super(Node, self).__init__()
        self.data = pos
        self.next = next
        self.prev = prev
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = settings.snake_color
        self.pos = pos

        # create a snake rect at (0,0) and then set correct position
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.settings.food_width, self.settings.food_height)
        self.rect.centerx = random.randrange(0+(self.settings.food_width/2), 500+(self.settings.food_width/2) , self.settings.food_height)
        self.rect.centery = random.randrange(0+(self.settings.food_width/2), 500+(self.settings.food_width/2) , self.settings.food_height)

        # Color of the snake head
        self.color = settings.snake_color

    def draw(self):
        """ Draw the snake to the screen """
        pg.draw.rect(self.screen,self.color,self.rect)

class Food():
    def __init__(self, settings, screen, snake):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.head = Node( self.screen, self.settings)
        self.tail = None
        self.coll = [snake.head.rect]
        self.snake = snake

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.growing = False

    def update(self):
        """ Draw the snake to the screen """
        if self.head.rect.collidelist(self.coll) >= 0:
            self.head.rect.centerx = random.randrange(0+(self.settings.food_width/2), 500+(self.settings.food_width/2) , self.settings.food_height)
            self.head.rect.centery = random.randrange(0+(self.settings.food_width/2), 500+(self.settings.food_width/2) , self.settings.food_height)
            self.snake.grow()
            self.draw()

    def draw(self):
        """ Draw the snake to the screen """
        self.head.draw()

    def spawn(self):
        #checking
        self.snake.grow()
        self.head.rect.centerx = random.randrange(0+(self.settings.food_width/2), 500+(self.settings.food_width/2) , self.settings.food_height)
        self.head.rect.centery = random.randrange(0+(self.settings.food_width/2), 500+(self.settings.food_width/2) , self.settings.food_height)
