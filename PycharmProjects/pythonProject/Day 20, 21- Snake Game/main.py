from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #este folosit pentru a nu mai avea imagini secventiale cand miscam segmentele(snake)
                 #si il setam la 0. Trebuie folosit in paralel cu screen.update() ca sa functioneze

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")  #am creat metode pentru fiecare din cele 4 comenzi in modulul snake
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # vezi mai sus la screen.tracer(0)
    time.sleep(0.1) #am importat modulul time pentru aceasta functionalitate care face display update la 0.1 secunde
    snake.move()

    #detect collision with food folosind metoda distance din Turtle
    if snake.head.distance(food) < 15:  # 15 reprezinta distanta dintre snake si food ca sa poate fi catalogata coliziunea
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()  #Facem display la aceasta funtie cu textul GAME OVER

    #detect colission with tail
    for segment in snake.segments: #sau pute adauga la snake.segments[1:] pentru a elimina primul segment din lista prin slicing
        if segment == snake.head:  #acesta este un workaround pentru ca initial va fi detectata o coliziune cu head-ul, dar folosind acest if, putem sa evitam
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

#############################################################
#ALTERNATIVA mai rudimentara a "for loop-ului de mai sus"
#segment_1 = Turtle("square")
#segment_1.color("white")
#segment_2 = Turtle("square")
#segment_2.color("white")
#segment_2.goto(-20, 0) #trebuie repozitionata pe axa XY (un patrat are 20/20. Deci avem acum - 20 (x) pe 0 (y)
#segment_3 = Turtle("square")
#segment_3.color("white")
#segment_3.goto(-40, 0)
##############################################################



















screen.exitonclick()