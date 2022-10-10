from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.speed("fast")
        segment.goto(position)
        segment.color("white")
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        segments = self.segments
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)

        segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
