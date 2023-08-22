import numpy as np
import arcade
import pymunk
import pygame

WIDTH = 1800
HEIGHT = 150
y_center = 525
button_size = 80
space = pymunk.Space
separation = 50

class Toolbar:

    def __init__(self):
        functions = ["triangle", "rectangle", "ellipse", "line", "free", "eraser", "select"]
        x_centers = [button_size*i+separation*(i-1) for i in range(1,8)]
        print(x_centers)
        self.buttons = [Button(func, i) for func, i in zip(functions, x_centers)]

    def draw(self):
        arcade.draw_rectangle_filled(900, 525, WIDTH, HEIGHT, arcade.color.AERO_BLUE)
        for button in self.buttons:
            button.draw()


class Button:
    def __init__(self, type, x_center):
        self.type = type
        self.x_center = x_center
        self.y_center = y_center
        self.x_start = x_center-button_size/2
        self.y_start = y_center+button_size/2
        self.clicked = False
        self.background_color = arcade.color.WHITE

    def isClicked(self,x, y):
        if(x>self.x_start and x<(self.x_start+button_size) and y<self.y_start and y>(self.y_start-button_size)):
            self.clicked = not self.clicked
            if self.clicked:
                self.background_color = arcade.color.WHITE_SMOKE
            else:
                self.background_color = arcade.color.WHITE
        return self.clicked

    def disable(self):
        self.clicked=False
        self.background_color = arcade.color.WHITE

    
    def draw(self):
        arcade.draw_rectangle_filled(self.x_center,self.y_center, button_size, button_size, self.background_color)