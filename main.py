import math
import arcade
import pymunk
import pygame
from objects import Polygon, Triangle

WIDTH = 1800
HEIGHT = 600
TITLE = "Paint"


class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        self.objects = []
        self.x_start=0
        self.y_start=0
        self.index=-1
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.x_start = x
            self.y_start = y
            self.index+=1
            self.draw=True
            self.objects.append(Polygon([(self.x_start, self.y_start)], arcade.color.AERO_BLUE, 5))
    
    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            self.x_end = x
            self.y_end = y
            self.objects[self.index].set_vertices(Triangle.collect_vertices(self.x_start, self.y_start, self.x_end, self.y_end))
        
    def on_draw(self):
        arcade.start_render()
        for object in self.objects:
            object.draw()


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()