import Snake, random, Eat, pygame

screen_width = 1000
screen_hight = 500
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
gray = (190, 190, 190)

snake_size = 10
eat_size = 10

buttons_1 = {
    pygame.K_LEFT: 'left',
    pygame.K_RIGHT: 'right',
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down',

}
buttons_2 = {
    pygame.K_w: 'up',
    pygame.K_s: 'down',
    pygame.K_a: 'left',
    pygame.K_d: 'right',
}


def get_super_color():
    return random.randint(20, 234), random.randint(20, 234), random.randint(20, 234)


def check_poz(snake):
    x = snake.get_next_step()
    eat = Eat.Eats.eat_array
    for i in eat:
        if i.locate[0] == x[0] and i.locate[1] == x[1]:
            i.respawn()
            snake.score += 1
            snake.grow()

    if x[0] >= screen_width:
        return snake.step_locate([0, x[1]])
    elif x[0] <= 0:
        return snake.step_locate([screen_width, x[1]])

    if x[1] >= screen_hight:
        return snake.step_locate([x[0], 0])
    elif x[1] <= 0:
        return snake.step_locate([x[0], screen_hight])
    return snake.step()


def movement_snake():
    for i in Snake.Snakes.snakes_array:
        check_poz(i)


def check_snakeDead(snake): #Проверка змеи на повреждение себя
    x = snake.locate[0]
    f = True
    for i in snake.locate:
        if f:
            f = False
            continue
        if i == x:
            return True
    return False


def check_all_snake_dead():
    snakes = Snake.Snakes.snakes_array
    touch = False
    for snake_1 in snakes:
        for snake_2 in snakes:
            if snake_1 == snake_2:
                if check_snakeDead(snake_1):
                    return True
            else:
                head = snake_1.locate[0]
                for body in snake_2.locate:
                    if head == body:
                        return True
    return touch


def check_button(snake):
    main_event = pygame.event.get()
    button1_bool = False
    button2_bool = False
    for event in main_event:
        if event.type == pygame.QUIT:
            return True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if len(Snake.Snakes.snakes_array) == 0:
                    Snake.Snakes(get_super_color())
                else:
                    Snake.Snakes.snakes_array = [Snake.Snakes.snakes_array[0]]


            if event.key == pygame.K_2:
                if len(Snake.Snakes.snakes_array) == 0:
                    Snake.Snakes(get_super_color())
                    Snake.Snakes(get_super_color())
                elif len(Snake.Snakes.snakes_array) == 1:
                    Snake.Snakes(get_super_color())
                else:
                    Snake.Snakes.snakes_array = [Snake.Snakes.snakes_array[0], Snake.Snakes.snakes_array[0]]



            if event.key in buttons_1 and not button1_bool:
                snake[0].get_turn(buttons_1[event.key])
                button1_bool = True

            if len(Snake.Snakes.snakes_array) == 2:
                if event.key in buttons_2 and not button2_bool:
                    snake[1].get_turn(buttons_2[event.key])
                    button2_bool = True











