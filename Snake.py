import random

import Game


class Snakes:
    def __init__(self, color):
        self.locate = [[random.randrange(10, Game.screen_width - 10, 10), random.randrange(10, Game.screen_hight - 10, 10)]]
        self.color = color
        self.id = Snakes.current_id
        Snakes.current_id += 1
        Snakes.snakes_array += [self]



    current_id = 0
    snakes_array = []
    score = 0
    size = 10
    dist_step = 10
    current_turn = 'none'
    turn = {
        'up': [0, -dist_step],
        'down': [0, dist_step],
        'left': [-dist_step, 0],
        'right': [dist_step, 0],
        'none': [0, 0]
    }

    def get_turn(self, new_turn):
        if self.current_turn == 'none':
            self.current_turn = new_turn
            return

        if new_turn == 'up':
            if self.current_turn != 'down':
                self.current_turn = new_turn
                return

        if new_turn == 'down':
            if self.current_turn != 'up':
                self.current_turn = new_turn
                return

        if new_turn == 'left':
            if self.current_turn != 'right':
                self.current_turn = new_turn
                return
        if new_turn == 'right':
            if self.current_turn != 'left':
                self.current_turn = new_turn
                return
        return

    def get_locate(self):
        return self.locate

    def step(self):
        for i in range(1, len(self.locate))[::-1]:
            self.locate[i][0] = self.locate[i-1][0]
            self.locate[i][1] = self.locate[i-1][1]

        self.locate[0][0] += self.turn[self.current_turn][0]
        self.locate[0][1] += self.turn[self.current_turn][1]

    def step_locate(self, locate):
        for i in range(1, len(self.locate))[::-1]:
            self.locate[i][0] = self.locate[i-1][0]
            self.locate[i][1] = self.locate[i-1][1]

        self.locate[0][0] = locate[0]
        self.locate[0][1] = locate[1]

    def grow(self):
        i = self.locate[0]
        eat_locate = [self.turn[self.current_turn][0] + i[0], self.turn[self.current_turn][1] + i[1]]
        self.locate = [eat_locate] + self.locate

    def get_next_step(self):
        i = self.locate[0]
        return [self.turn[self.current_turn][0] + i[0], self.turn[self.current_turn][1] + i[1]]

















