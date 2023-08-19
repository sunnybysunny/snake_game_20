from turtle import Screen
import time

from snake import Snake
from food import Food

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game Time")
screen.tracer(0)

# create a snake and food objects
snake = Snake()
food = Food()

# listen for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move snake
game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(.1)


screen.exitonclick()
