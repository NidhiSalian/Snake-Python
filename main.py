from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()

food = Food()

game_is_on = True

screen.listen()
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)

scoreboard = ScoreBoard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check for collision with food
    if snake.head.distance(food) <= 15:
        scoreboard.increment_score()
        snake.add_segment()
        food.reposition()

    # Detect collision with wall:
    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail:
    if snake.detect_collision():
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
