from turtle import Turtle, Screen
import time

from snake import Snake

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game Time")
# screen.tracer(0)



# Create Snake Body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake = Snake(positions=starting_positions)


# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)


# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(.1)
#     #snake.move()
#     for seg_num in range(len(segments) - 1, 0, -1):  # start = 2, stop= 0, step = - 1
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#
#     segments[0].forward(20)

screen.exitonclick()
