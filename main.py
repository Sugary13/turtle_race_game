from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Haz tu apuesta.", prompt="¿Que tortuga ganara la carrera? Escribe su nombre: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-70+(30*turtle_index))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
                break
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
                break


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
