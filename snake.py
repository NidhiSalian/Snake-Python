from turtle import Turtle

LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.head = None
        self.move_distance = 20
        for _ in range(3):
            self.add_segment()

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")

        if len(self.segments) == 0:
            self.head = new_segment
        else:
            last_segment = self.segments[-1]
            new_segment.goto(last_segment.xcor() + 20, last_segment.ycor())
        self.segments.append(new_segment)

    def detect_collision(self):
        has_collided = False
        if len(self.segments) <= 3:
            return has_collided
        for segment in self.segments[3:]:
            if self.head.distance(segment) < 10:
                has_collided = True
                break
        return has_collided

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            prev_segment = self.segments[i-1]
            self.segments[i].goto(prev_segment.xcor(), prev_segment.ycor())
        self.head.forward(self.move_distance)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
