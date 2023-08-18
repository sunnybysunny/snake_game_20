from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)


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