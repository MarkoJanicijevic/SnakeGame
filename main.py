from turtle import Turtle, Screen
import time
from snake import *
from food import *
from scoreboard import *


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()


game_is_on = True

snake = Snake()
food = Food()
score = Score()


screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")




while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

#detect collision with food

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        new_pos = snake.segments[-1].position()
        snake.create_segment(new_pos)


#detect collision with wall

    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 295 or snake.snake_head.ycor() < -295:
        score.game_over()
        game_is_on = False

#detect collision with tail

    for segment in snake.segments[2:]:
        if snake.snake_head.distance(segment) < 10:
            score.game_over()
            game_is_on = False





























screen.exitonclick()