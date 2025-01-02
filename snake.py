
from turtle import Turtle
LIST_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]
        self.snake_head.shape("triangle")

    def create_snake(self):
        for pos in LIST_POSITIONS:
            self.create_segment(pos)

    def move_snake(self):
        for s in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[s - 1].position()
            self.segments[s].goto(new_pos)
        self.snake_head.forward(20)

    def go_left(self):
        self.snake_head.setheading(180)

    def go_right(self):
        self.snake_head.setheading(0)

    def go_up(self):
        self.snake_head.setheading(90)

    def go_down(self):
        self.snake_head.setheading(270)

    def create_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)


    def snake_reset(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]
        self.snake_head.shape("triangle")