import turtle

screen=turtle.Screen()
screen.title("Ze FLYING TURTLE HAS ARRIVED")
screen.bgcolor("white")

t=turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(3)
t.pensize(2)

def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)


pen_down=True

def toggle_pen():
    global pen_down
    if pen_down:
        t.penup()
        pen_down = False
    else:
        t.pendown()
        pen_down = True

def clear_and_reset():
    t.clear()
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.pendown()

screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.onkey(toggle_pen,"space")
screen.onkey(clear_and_reset,"c")

turtle.done()