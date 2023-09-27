from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #aici am creat un tuple pt a pastra mereu aceste valori
MOVE_DISTANCE = 20   # acestea sunt CONSTANTE, valori fixe
UP = 90  #am creat aceste constante pentru a implementa o regula, mai exact aceea de a evita miscarea inainte si inapoi a sarpelui, ceea ce presupune schimbarea head-ului
DOWN = 270
LEFT = 180
RIGHT = 0




class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #aici doar specificam care este "capul" pentru a nu mai scrie de fiecare data

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position): #din functia de mai sus - create_snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # pentru a elimina linia pe care o lasa in urma
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())   # -1 semnifica ultimul element din lista, spre exemplu segments = (1, 2, 3), -1 reprezinta nr 3

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # acest range(start=2, stop=0 , step=-1) este pentru a executa pozitia unui segment
                                                              # dar in sens invers (ex: 3, 2, 1)
                                                              # pe pozitia "start" am pus len(segments) - 1 pentru a aduce de fiecare data ultimul numar de segmente, pentru ca acesta va creste mereu dinamic
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  #acest if este pentru a evita posibilitatea de a merge inapoi, implicit in directia opusa pentru fiecare din comenzile de mai jos
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

