from turtle import Turtle


class Snake:
    def __init__(self, positions,):
        self.positions = positions
        self.segments = []

        for pos in positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move_snake(self):
        pass







#create a Snake class that creates our three little squares
# create a method snake.move() that moves our snake forward