import arcade
import pymunk
from objects import Triangle, Rectangle, Ellipse, Line, Free
import interface
from interface import Toolbar
WIDTH = 1400
HEIGHT = 900
TITLE = "Paint"
space = pymunk.Space
toolbar_height = interface.HEIGHT
background_color = arcade.color.WHITE

class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(background_color)
        self.objects = []
        self.x_start=0
        self.y_start=0
        self.index=-1
        self.toolbar = Toolbar()
        self.drawing = False
        self.pen_color = arcade.color.BLACK
        self.pen_thickness = 2
        self.active = self.toolbar.buttons[4]
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if(y<(HEIGHT-toolbar_height)):
                self.drawing = True
                self.x_start = x
                self.y_start = y
                self.draw=True
                self.clicked = True
                self.objects.append(self.set_figure())
            else:
                self.drawing=False
                for button in self.toolbar.buttons:
                    if button.is_clicked(x,y):
                        self.active = button
                for color in self.toolbar.colors:
                    self.pen_color = color.is_clicked(x,y,self.pen_color)
                for thickness in self.toolbar.thickness_buttons:
                    if thickness.is_clicked(x,y):
                        self.pen_thickness = thickness.get_thickness()
    
    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if buttons == arcade.MOUSE_BUTTON_LEFT and self.drawing:
            self.x_end = x
            self.y_end = y
            if(self.active.type=="free" or self.active.type=="eraser"):
                self.objects[-1].add_point(x, y)
            else:
                self.objects[-1].collect_vertices(self.x_start, self.y_start, self.x_end, self.y_end)
    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        return super().on_mouse_motion(x, y, dx, dy)

    def set_figure(self):
        if self.active.type == "triangle":
            return Triangle(self.pen_color, self.pen_thickness)
        elif self.active.type == "rectangle":
            return Rectangle(self.pen_color, self.pen_thickness)
        elif self.active.type == "ellipse":
            return Ellipse(self.pen_color, self.pen_thickness)
        elif self.active.type == "line":
            return Line(self.pen_color, self.pen_thickness)
        elif self.active.type == "free":
            return Free(self.pen_color, self.pen_thickness)
        elif self.active.type == "eraser":
            return Free(background_color, self.pen_thickness)

    def on_draw(self):
        arcade.start_render()
        for object in self.objects:
            if object.set_vertices:
                object.draw()
        self.toolbar.draw()


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()