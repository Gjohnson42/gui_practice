"""
This program is an example of the fundamental parts of a user interface: a sprite button hooked up to a function.
It takes arcade for the ability to draw windows and set up buttons, os for being able to pull in sprite files.

"""

import arcade

# This here lets me get information on sprite size.
from PIL import Image

# Global Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
SCREEN_TITLE = "Button GUI"


# Declaring a MyGame class, subclass of Window.
class MyGame(arcade.Window):

    # defining constructor, calling superclass
    def __init__(self, background_color):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN_TITLE)

        # declaring fields
        self.button_x = 0
        self.button_y = 0
        self.times_pressed = 0
        self.button_sprite_list = None

        # loading background color
        arcade.set_background_color(background_color)

    def setup(self):
        # setting button location values
        self.button_x = WINDOW_WIDTH // 2
        self.button_y = WINDOW_HEIGHT // 2

        #  TODO appending button sprite to sprite list
        self.button_sprite_list = arcade.SpriteList()
        self.button_sprite = arcade.Sprite(r"C:\Users\Garrett\Pictures\py_sprites\blue_button.jpg")
        self.button_sprite_list.append(self.button_sprite)

        # Setting the button in the proper place
        self.button_sprite.center_x = self.button_x
        self.button_sprite.center_y = self.button_y

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("This button has been pushed " + str(self.times_pressed) + " times.",
                         200, 500, arcade.color.BLACK)
        self.button_sprite_list.draw()

    def update(self, delta_time: float):
        self.button_sprite_list.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Defining variables for button location
        button_x_lower = self.button_sprite.center_x - (self.button_sprite.width / 2)
        button_x_upper = self.button_sprite.center_x + (self.button_sprite.width / 2)

        button_y_lower = self.button_sprite.center_y - (self.button_sprite.height / 2)
        button_y_upper = self.button_sprite.center_y + (self.button_sprite.height / 2)

        on_button_location = button_x_lower < x < button_x_upper and button_y_lower < button_y_upper

        if on_button_location and button == arcade.MOUSE_BUTTON_LEFT:
            self.times_pressed += 1

def main():
    game = MyGame(arcade.color.WHITE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
