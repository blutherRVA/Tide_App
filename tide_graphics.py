import time_keeper
import turtle
turt = turtle.Turtle()
turt.hideturtle()


def james_animation(time_stamp):
    james_t = turtle.Turtle()
    james_t.hideturtle()
    james_t.color("cyan")
    james_t.penup()
    t = time_keeper.time_keeper(time_stamp)
    if t < 22350:
        y = (-130 + (280*(t/22350)))
        james_t.goto(-400, y)
        james_t.lt(90)
        james_t.showturtle()
    elif t >= 22350:
        y = (150 - (280 * ((t - 22350) / 22350)))
        james_t.goto(-400, y)
        james_t.rt(90)
        james_t.showturtle()
    else:
        print("James Animation Error")



def piank_animation(time_stamp):
    piank_t = turtle.Turtle()
    piank_t.hideturtle()
    piank_t.color("cyan")
    piank_t.penup()
    t = time_keeper.time_keeper(time_stamp)
    if t < 22350:
        y = (-130 + (280*(t/22350)))
        piank_t.goto(0, y)
        piank_t.lt(90)
        piank_t.showturtle()
    elif t >= 22350:
        y = (150 - (280 * ((t - 22350) / 22350)))
        piank_t.goto(0, y)
        piank_t.rt(90)
        piank_t.showturtle()
    else:
        print("Piankatank Animation Error")

def mobjack_animation(time_stamp):
    mobjack_t = turtle.Turtle()
    mobjack_t.hideturtle()
    mobjack_t.color("cyan")
    mobjack_t.penup()
    t = time_keeper.time_keeper(time_stamp)
    if t < 22350:
        y = (-130 + (280*(t/22350)))
        mobjack_t.goto(400, y)
        mobjack_t.lt(90)
        mobjack_t.showturtle()
    elif t >= 22350:
        y = (150 - (280 * ((t - 22350) / 22350)))
        mobjack_t.goto(400, y)
        mobjack_t.rt(90)
        mobjack_t.showturtle()
    else:
        print("Mobjack Animation Error")