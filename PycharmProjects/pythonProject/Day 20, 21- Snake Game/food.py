from turtle import Turtle
import random

#Vom face din clasa Food o subclasa a clasei turtle, avand toate atributiile acesteia + modificari

class Food(Turtle):   #am adaugat superclasa corerspunzatoare
  # self.food = Turtle() #am creat un atribut din clasa turtle, dar nu vrem asta, este doar ca exemplu
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #by default este 20/20 ca si patratele sarpelui, dar vrem sa o facem mai mica, de 10/10
        self.color("yellow")
        self.speed("fastest")
        #random_x = random.randint(-280, 280)   #Am pus o locatie random pentru mancare/food pe axa XY, dar mai mica decat limita ecranului de 300/300 pentru a fi mai usor de jucat
        #random_y = random.randint(-280, 280)
        #self.goto(random_x, random_y)
        self.refresh()



    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)