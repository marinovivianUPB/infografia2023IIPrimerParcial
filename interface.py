import numpy as np
import arcade
import pymunk
import pygame
from objects import Triangle, Rectangle

WIDTH = 1800
HEIGHT = 150
y_center = 525
button_size = 80
space = pymunk.Space
separation = 50
green = arcade.color.MOSS_GREEN
red = arcade.color.REDWOOD

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
        print("disabled")
    
    def draw(self):
        arcade.draw_rectangle_filled(self.x_center,self.y_center, button_size, button_size, self.background_color)
        self.figure()

    def figure(self):
        if self.type == "triangle":
            arcade.draw_polygon_outline(Triangle.collect_vertices(self.x_start+10, self.y_start-10, self.x_start+button_size-10, self.y_start-button_size+10), green, 2)
        elif self.type == "rectangle":
            arcade.draw_polygon_outline(Rectangle.collect_vertices(self.x_start+10, self.y_start-10, self.x_start+button_size-10, self.y_start-button_size+10), green, 2)
        elif self.type == "ellipse":
            arcade.draw_ellipse_outline(self.x_center, self.y_center, button_size-10, button_size-20, green, 2)
        elif self.type == "line":
            arcade.draw_line(self.x_start+10, self.y_start-10, self.x_start+button_size-10, self.y_start-button_size+10, green, 2)
        elif self.type =="free" or self.type=="eraser" or self.type=="select":
            arcade.draw_text(self.type, self.x_start, self.y_center, green, 12, button_size, "center")