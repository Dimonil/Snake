import pygame
import Game
import Snake
import Eat


def draw_snake(_snake, _dis):
    for i in _snake.locate:
        pygame.draw.rect(_dis, _snake.color, [i[0], i[1], Game.snake_size, Game.snake_size])


def draw_eat(_dis):
    for _eat in Eat.Eats.eat_array:
        pygame.draw.rect(_dis, _eat.color, [_eat.locate[0], _eat.locate[1], Game.eat_size, Game.eat_size])


def draw_all_snake(snake_array, dis):
    for i in snake_array:
        draw_snake(i, dis)


def draw_all_eat(eat_array, dis):
    for i in eat_array:
        draw_eat(dis)


class Displays:
    def __init__(self):
        pygame.init()
        self.game = Game
        self.dis = pygame.display.set_mode((self.game.screen_width, self.game.screen_hight))
        self.display = pygame.display
        self.display.set_caption('Snake game!')
        self.dis.fill(self.game.gray)

    place_4_message = [[Game.screen_width / 4, Game.screen_hight / 10], [Game.screen_width - (Game.screen_width / 4), (Game.screen_hight / 10)]]

    def display_update(self):
        self.display.update()

    def draw_object(self):

        self.dis.fill(self.game.gray)
        self.draw_message_score()

        draw_all_snake(Snake.Snakes.snakes_array, self.dis)
        draw_all_eat(Eat.Eats.eat_array, self.dis)
        self.display_update()

    def display_quit(self):
        self.display.set_caption('GG')
        pygame.quit()


    def draw_menu(self):
        self.dis.fill(self.game.gray)
        pygame.draw.rect(self.dis, Game.blue, )


    def message(self, msg, color, num_message):
        msg = str(msg)
        font_style = pygame.font.SysFont(None, int(Game.screen_width / 20))
        mesg = font_style.render(msg, True, color)
        self.dis.blit(mesg, self.place_4_message[num_message])

    def draw_message_score(self):
        score = 'Snake game!        '
        count = 0
        for snake in Snake.Snakes.snakes_array[::-1]:
            count += 1
            '''self.message('Your score : ' + str(snake.score), snake.color, snake.id)'''
            score += f'     snake {count} : {str(snake.score)}'

        self.display.set_caption(score)
