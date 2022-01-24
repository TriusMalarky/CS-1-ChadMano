# Zachary Tueller  
# CS1400 - MO1
# Assignment 2

import turtle as tr

if __name__ == "__main__":
    locY = int(input("Enter the Y position of the bullseye:\n: "))
    locX = int(input("Enter the X position of the bullseye:\n: "))
    radius = int(input("Enter the radius of the bullseye:\n: ")) * 3

    s = tr.getscreen()  # init screen
    t = tr.Turtle()
    t.ht()
    t.up()
    s.title("Robin Hood")  # define screen title/caption

    def drawCircle(t,color,radius,X,Y):
        t.goto(X, Y)
        t.color(color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    drawCircle(t, 'black', radius * 4,locX,locY)
    drawCircle(t, 'blue', radius * 3,locX, locY + radius)
    drawCircle(t, 'red', radius * 2, locX, locY + (radius * 2))
    drawCircle(t, 'green', radius, locX, locY + (radius * 3))

    exit = input("Exit? Y/N: ")

