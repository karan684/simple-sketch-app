from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
#tim.setheading(90)

def move_up():
    tim.forward(10)

def move_down():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun = move_up)
screen.onkey(key="s", fun = move_down)
screen.onkey(key="a", fun = move_left)
screen.onkey(key="d", fun = move_right)
screen.onkey(key="c", fun = clear_screen)
screen.exitonclick()