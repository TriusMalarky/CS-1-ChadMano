# Zachary Tueller  
# CS1400 - MO1
# Assignment 1

import turtle as t

def task1():
    s = t.getscreen() # init screen
    tr = t.Turtle()
    s.title("Why are there so many songs about snowmen?") # define screen title/caption
    tr.ht()

    # vv body
    tr.fillcolor("white")
    tr.goto(0,-200);tr.begin_fill();tr.circle(120);tr.end_fill();tr.circle(120,180)
    tr.goto(0,150);tr.begin_fill();tr.circle(80);tr.end_fill()
    tr.goto(0,220);tr.begin_fill();tr.circle(60);tr.end_fill()
    # ^^ end body

    # vv eyes
    tr.fillcolor("black")
    tr.up();tr.goto(-20,180);tr.dot(30);tr.goto(20,180);tr.dot(30)
    # ^^ end eyes

    # vv moustache
    tr.fillcolor("purple")
    tr.goto(3,150);tr.down();tr.circle(120,-15);tr.up()
    tr.up();tr.goto(-3,150);tr.down();tr.circle(120,15)
    # ^^moustache

    # vv mouth
    tr.pencolor("red");tr.pensize(5)
    tr.up();tr.goto(-20,120);tr.down();tr.goto(20,120)
    # ^^ mouth

    # vv buttons
    tr.pencolor("green");tr.up()
    tr.goto(0,80);tr.dot();tr.goto(0,50);tr.dot();tr.goto(0,20);tr.dot()
    # ^^ buttons

    # vv arms
    tr.pencolor("brown")