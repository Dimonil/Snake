import random
import Display
import Game
import Snake
import Eat
import pygame


def get_super_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


display = Display.Displays()


def run_game():
    snake = Snake.Snakes(get_super_color())
    Eat.Eats()
    Eat.Eats()
    game_over = False
    clock = pygame.time.Clock()
    ticks = pygame.time

    while not game_over:
        clock.tick(20)
        display.draw_object()
        display.game.movement_snake()
        game_over = Game.check_button(Snake.Snakes.snakes_array)
        if game_over:
            pygame.quit()
            quit()
        if Game.check_all_snake_dead():
            Snake.Snakes.snakes_array = []
            Eat.Eats.eat_array = []
            return True


def play():
    while run_game():
        pass



play()


'''был выбор для 1 или 2 игроков'''