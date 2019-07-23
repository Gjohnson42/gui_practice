import arcade

# Global Constants

GAME_TITLE = "Band of Delvers"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


# Class declarations first
class MyGame(arcade.Window):
    # Def Statements, non-composite functions first

    # Constructor
    def __init__(self, width, height, title, bg_color):
        # calls superclass constructor explicitly
        super().__init__(width, height, title)

        # sets the background
        arcade.set_background_color(bg_color)

        # initializing values from constructor arguments
        self.title = title
        self.width = width
        self.height = height
        self.position = 50
        self.velocity = 5
        self.radius = 30

    # The on_draw function is a special name, and it gets called when a new frame is to be rendered.
    def on_draw(self):
        arcade.start_render()
        x = self.width / 2
        y = self. width / 2
        message = self.title + ": " + str(self.position)
        arcade.draw_circle_filled(self.position, y, self.radius, arcade.color.RED_ORANGE)

    def reverse_direction(self):
        self.velocity *= -1

    def update(self, delta_time: float):
        # Setting up a couple booleans to check if it's at the left or right edge
        at_right = self.position > self.width-self.radius
        at_left = self.position < self.radius and self.velocity < 0
        if at_left or at_right:
            self.reverse_direction()
        self.position += self.velocity

    # now this is new. You're setting up an event listener, for left and right keys.
    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.SPACE:
            self.reverse_direction()


def main():
    # Creates an instance of a game object.
    game = MyGame(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, arcade.color.BITTER_LIME)
    game.position = 1
    arcade.run()


# This bit of code checks to make sure that this file isn't being imported before running main()


if __name__ == '__main__':
    main()
