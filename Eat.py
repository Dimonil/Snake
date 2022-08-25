import Game
import random


class Eats:
    def __init__(self):

        self.locate = [random.randrange(0, Game.screen_width - 10, 10), random.randrange(0, Game.screen_hight - 10, 10)]
        self.color = Eats.eat_color
        Eats.eat_array += [self]

    eat_array = []
    eat_color = (50, 50, 50)

    def respawn(self):
        self.locate = [random.randrange(0, Game.screen_width - 10, 10), random.randrange(0, Game.screen_hight - 10, 10)]

    @classmethod
    def destroy(cls):
        Eats.eat_array = []

    @classmethod
    def show_eats(cls):
        x = []
        for i in Eats.eat_array:
            x += [i.locate]
        print(x)