import numpy as np
import arcade
import pymunk
import pygame
from objects import Triangle, Rectangle

WIDTH = 1800
HEIGHT = 150
y_center = 900-75
button_size = 80
color_box_size=20
line_size=60
space = pymunk.Space
separation = 50
green = arcade.color.MOSS_GREEN
red = arcade.color.REDWOOD

class Toolbar:

    def __init__(self):
        functions = ["triangle", "rectangle", "ellipse", "line", "free", "eraser"]
        x_centers = [button_size*i+separation*(i-1) for i in range(1,7)]
        self.buttons = [Button(func, i) for func, i in zip(functions, x_centers)]
        self.colors=[]
        for i in range(3):
            self.colors+=self.define_colors(x_centers[-1], 900-50-30*i)
        self.colors[0].color = [(0,0,0)]
        thick_values=[i for i in range(2,9,2)]
        y_values=[900-20-i-20*i for i in thick_values]
        self.thickness_buttons=[Thickness_Button(val, 1800-60, i) for val, i in zip(thick_values, y_values)]
        

    def define_colors(self, start, y_center):
        colors_per_row=10
        x_centers = [start+button_size/2+color_box_size*i+(separation/5)*i-1 for i in range(1,colors_per_row+1)]
        red = np.random.randint(0, 256, size=colors_per_row)
        green = np.random.randint(0, 256, size=colors_per_row)
        blue = np.random.randint(0, 256, size=colors_per_row)
        return [Color_Box(r,g,b, y_center, i) for r,g,b,i in zip(red, green, blue, x_centers)]

    def draw(self):
        arcade.draw_rectangle_filled(900, y_center, WIDTH, HEIGHT, arcade.color.AERO_BLUE)
        for button in self.buttons:
            button.draw()
        for color in self.colors:
            color.draw()
        for thick in self.thickness_buttons:
            thick.draw()


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
        self.figure()

    def figure(self):
        if self.type == "triangle":
            self.icon = Triangle(green, 2)
            self.icon.collect_vertices(self.x_start+10, self.y_start-10, self.x_start+button_size-10, self.y_start-button_size+10)
            self.icon.draw()
        elif self.type == "rectangle":
            self.icon = Rectangle(green, 2)
            self.icon.collect_vertices(self.x_start+10, self.y_start-10, self.x_start+button_size-10, self.y_start-button_size+10)
            self.icon.draw()
        elif self.type == "ellipse":
            arcade.draw_ellipse_outline(self.x_center, self.y_center, button_size-10, button_size-20, green, 2)
        elif self.type == "line":
            arcade.draw_line(self.x_start+10, self.y_start-10, self.x_start+button_size-10, self.y_start-button_size+10, green, 2)
        elif self.type =="free" or self.type=="eraser":
            arcade.draw_text(self.type, self.x_start, self.y_center, green, 12, button_size, "center")


class Color_Box:
    def __init__(self, red, green, blue, y_center, x_center):
        self.color = [(red,green,blue)]
        print(self.color)
        self.y_center = y_center
        self.x_center = x_center
        self.x_start = x_center-color_box_size/2
        self.y_start = y_center+color_box_size/2
    
    def isClicked(self,x, y, color):
        if(x>self.x_start and x<(self.x_start+color_box_size) and y<self.y_start and y>(self.y_start-color_box_size)):
            return self.color[0]
        else:
            return color
    
    def draw(self):
        arcade.draw_rectangle_outline(self.x_center,self.y_center,color_box_size+1,color_box_size+1, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.x_center,self.y_center,color_box_size,color_box_size, self.color[0])

class Thickness_Button:
    def __init__(self, value, x_center, y_center):
        self.value=value
        self.x_start = x_center-line_size/2
        self.y_start = y_center
    
    def draw(self):
        arcade.draw_line(self.x_start, self.y_start, self.x_start+line_size, self.y_start, arcade.color.BLACK, self.value)