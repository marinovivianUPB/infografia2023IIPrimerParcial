import numpy as np
import arcade
import math

class Polygon:
    def __init__(self, vertices, color, thickness):
        self.vertices = vertices
        self.color = color
        self.thickness = thickness
    
    def set_vertices(self, vertices):
        self.vertices = []
        for vert in vertices:
            self.vertices.append(vert)
        print(self.vertices)
    
    def set_color(self, color):
        self.color = color
    
    def draw(self):
        if(len(self.vertices) == 1):
            arcade.draw_point(self.vertices[0][0], self.vertices[0][1], self.color, self.thickness)
        else:
            arcade.draw_polygon_outline(self.vertices, self.color, self.thickness)

class Triangle:
    def collect_vertices(x_start, y_start, x_end, y_end):
        height  = abs(y_end-y_start)
        width = abs(x_end-x_start)
        if y_start > y_end:
            sign_y=-1
        else:
            sign_y=1

        if x_start > x_end:
            sign_x=-1
        else:
            sign_x=1
        vertices = []
        vertices.append((x_start, y_start))
        vertices.append((x_start+width*sign_x, y_start))
        vertices.append((x_start+(width*sign_x)/2, y_start+height*sign_y))
        return vertices

class Rectangle:
    def collect_vertices(x_start, y_start, x_end, y_end):
        height  = abs(y_end-y_start)
        width = abs(x_end-x_start)
        if y_start > y_end:
            sign_y=-1
        else:
            sign_y=1

        if x_start > x_end:
            sign_x=-1
        else:
            sign_x=1
        vertices = []
        vertices.append((x_start, y_start))
        vertices.append((x_start+width*sign_x, y_start))
        vertices.append((x_start+(width*sign_x), y_start+height*sign_y))
        vertices.append((x_start, y_start+height*sign_y))
        return vertices