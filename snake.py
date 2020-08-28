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
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.settings.snake_width, self.settings.snake_height)
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]

        # Color of the snake head
        self.color = settings.snake_color

    def draw(self):
        """ Draw the snake to the screen """
        pg.draw.rect(self.screen,self.color,self.rect)

class Snake():
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.head = Node( self.screen, self.settings)
        self.tail = None

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.growing = False

        self.coll = []

    def grow(self):

        if self.tail == None:
            self.head.next = Node( self.screen, self.settings, self.head.data)
            self.coll.append(self.head.next)
            self.tail = self.head.next
            self.growing = False
        else:
            self.tail.next = Node( self.screen, self.settings, self.tail.data)
            self.coll.append(self.tail.next)
            self.tail = self.tail.next
            self.growing = False

    def draw(self):
        """ Draw the snake to the screen """
        curr_node = self.head
        curr_node.draw()
        while curr_node.next != None:
            curr_node.next.draw()
            curr_node = curr_node.next

    def update(self):

        """ Move the snakes location """
        #Update the decimal position of the snake.

        curr_node = self.head
        change = False



        if self.moving_right:
            change = True
            curr_node.data[0] = curr_node.rect.centerx
            curr_node.data[1] = curr_node.rect.centery
            curr_node.rect.centerx = curr_node.rect.centerx + self.settings.snake_speed_factor


        if self.moving_left:
            change = True
            curr_node.data[0] = curr_node.rect.centerx
            curr_node.data[1] = curr_node.rect.centery
            curr_node.rect.centerx = curr_node.rect.centerx - self.settings.snake_speed_factor

        if self.moving_up:
            change = True
            curr_node.data[0] = curr_node.rect.centerx
            curr_node.data[1] = curr_node.rect.centery
            curr_node.rect.centery = curr_node.rect.centery - self.settings.snake_speed_factor

        if self.moving_down:
            change = True
            curr_node.data[0] = curr_node.rect.centerx
            curr_node.data[1] = curr_node.rect.centery
            curr_node.rect.centery = curr_node.rect.centery + self.settings.snake_speed_factor

        if self.growing:
            self.grow()

        if self.head.rect.collidelist(self.coll) >= 0:
            print("SCORE: " + str(len(self.coll)))
            print("Loser")
            sys.exit()

        if change == True:
            while curr_node.next:
                x = curr_node.data[0]
                y = curr_node.data[1]
                curr_node = curr_node.next

                curr_node.data[0] = curr_node.rect.centerx
                curr_node.data[1] = curr_node.rect.centery

                curr_node.rect.centerx = x
                curr_node.rect.centery = y

            change = False
