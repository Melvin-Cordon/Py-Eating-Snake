import sys
import random

import pygame as pg
from pygame.sprite import Sprite

class Node(Sprite):
    def __init__(self, screen, settings, pos = None, prev_pos = None, next = None, prev = None):
        super(Node, self).__init__()
        self.data = pos
        self.next = next
        self.prev = prev
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = settings.snake_color


        # create a snake rect at (0,0) and then set correct position
        self.rect = pg.Rect(0, 0, self.settings.snake_width, self.settings.snake_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Color of the snake head
        self.color = settings.snake_color

    def draw(self):
        """ Draw the snake to the screen """
        print('here')
        pg.draw.rect(self.screen,self.color,self.rect)

class Snake():
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.head = Node( self.screen, self.settings, [0,0])

    def insert_end(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head

        curr_node = self.tail
        curr_node.next = Node(val, None, curr_node)
        self.tail = curr_node.next

    def draw(self):
        """ Draw the snake to the screen """
        curr_node = self.head
        curr_node.draw()
        while curr_node.next != None:
            curr_node.draw()
            curr_node = curr_node.next
