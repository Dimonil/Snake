import Display
import Snake
import Eat


game = False
snake = Snake.Snakes((120,120,120))
display_1 = Display.Displays()
display_2 = Display.Displays()
Eat.Eats()

while not game:
    display_1.draw_object()
    display_2.draw_object()



