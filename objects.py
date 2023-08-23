import numpy as np
import arcade

class Figure:
    def __init__(self, color, thickness):
        self.vertices=[]
        self.color = color
        self.thickness = thickness
        self.setVertices = False

class Triangle(Figure):

    def __init__(self, color, thickness):
        super().__init__( color, thickness)

    def collect_vertices(self, x_start, y_start, x_end, y_end):
        self.setVertices=True
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
        self.vertices = vertices
        return vertices
    
    def draw(self):
        if(len(self.vertices) == 1):
            arcade.draw_point(self.vertices[0][0], self.vertices[0][1], self.color, self.thickness)
        else:
            arcade.draw_polygon_outline(self.vertices, self.color, self.thickness)

class Rectangle(Figure):

    def __init__(self, color, thickness):
        super().__init__( color, thickness)

    def collect_vertices(self, x_start, y_start, x_end, y_end):
        self.setVertices=True
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
        self.vertices = vertices
        return vertices
    
    def draw(self):
        if(len(self.vertices) == 1):
            arcade.draw_point(self.vertices[0][0], self.vertices[0][1], self.color, self.thickness)
        else:
            arcade.draw_polygon_outline(self.vertices, self.color, self.thickness)

class Ellipse(Figure):

    def __init__(self, color, thickness):
        super().__init__( color, thickness)

    def collect_vertices(self, x_start, y_start, x_end, y_end):
        self.setVertices=True
        self.height  = abs(y_end-y_start)
        self.width = abs(x_end-x_start)
        if y_start > y_end:
            sign_y=-1
        else:
            sign_y=1

        if x_start > x_end:
            sign_x=-1
        else:
            sign_x=1
        vertices = []
        vertices.append((x_start+sign_x*self.width/2, y_start+sign_y*self.height/2))
        self.vertices = vertices
        return vertices
    
    def draw(self):
        if(not self.setVertices):
            arcade.draw_point(self.vertices[0][0], self.vertices[0][1], self.color, self.thickness)
        else:
            arcade.draw_ellipse_outline(self.vertices[0][0], self.vertices[0][1], self.width, self.height, self.color, self.thickness)

class Line(Figure):

    def __init__(self, color, thickness):
        super().__init__( color, thickness)

    def collect_vertices(self, x_start, y_start, x_end, y_end):
        self.setVertices=True
        vertices = []
        vertices.append((x_start, y_start))
        vertices.append((x_end, y_end))
        self.vertices = vertices
        return vertices
    
    def draw(self):
        if(len(self.vertices)==1):
            arcade.draw_point(self.vertices[0][0], self.vertices[0][1], self.color, self.thickness)
        else:
            arcade.draw_line(self.vertices[0][0], self.vertices[0][1], self.vertices[1][0], self.vertices[1][1], self.color, self.thickness)
        
class Free(Figure):

    def __init__(self, color, thickness):
        super().__init__( color, thickness)
        self.points = []
    
    def add_point(self, x ,y):
        self.setVertices=True
        self.points.append((x,y))
    
    def draw(self):
        for i in range(len(self.points)-1):
            arcade.draw_line(self.points[i][0], self.points[i][1], self.points[i+1][0], self.points[i+1][1], self.color, self.thickness)