import random
import Display
import Game
import Snake
import Eat
import pygame


def get_super_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def Run_game():

    display = Display.Displays()
    snake = Snake.Snakes(get_super_color())
    snake2 = Snake.Snakes(get_super_color())
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

        if Game.check_all_snake_dead():
            break


Run_game()
pygame.quit()
quit()

'''был выбор для 1 или 2 игроков'''