# Zachary Tueller  
# CS1400 - MO1
# Assignment 2

import math

if __name__ == "__main__":
    numSides = int(input("How many sides will this polygon have:\n: "))
    length = float(input("How long are each of these sides?\n: "))
    unit = input("What unit would you like to use?\n: ")

    area = (numSides * math.pow(length, 2)) / (4 * (math.tan(math.pi / numSides)))
    string = "The area of the polygon is " + str(area) + " " + unit + " squared"
    print(string)