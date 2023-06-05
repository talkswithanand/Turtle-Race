from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height= 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: " )
colors = ["red", "orange", "yellow", "blue", "green", "purple"]

y_incr = 50
i = 0
all_turtles = []

for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x= -230, y =-170 + y_incr)
    y_incr += 50
    i += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            winning_turtle = turtles.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f" You have won! The {winning_turtle} turtle is the winner.")
            else:
                print(f" You have lost! The {winning_turtle} turtle is the winner.")

        rand_distance = random.randint(0,10)
        turtles.forward(rand_distance)


screen.exitonclick()