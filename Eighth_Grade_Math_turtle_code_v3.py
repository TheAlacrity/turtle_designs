
import turtle

from menu import colorMenu

def eighthGradeMath():

    turtle.clear()

    turtle.ht() # hides turtle

    faster = int(input("How fast? 1-10, 1 is slow, 10 is fast:  "))

    turtle.speed(faster)

    pixel = int(input("Pixel separation (smaller numbers give more detail):  "))

    size = float(input("Size multiplier:  "))
    
    q = (size * pixel) / 10

    sizeN = size / 10

    # 1st drawn quadrant (math quadrant I, 0-90)
    X = 0
    Y = q
    count = 0
    while count <= sizeN:

        turtle.setpos(0, Y)
        turtle.pendown()
        turtle.goto(X, 0)
        turtle.penup()

        X += pixel
        Y -= pixel
                 
        count += 1

    turtle.setpos(0, 0)

    # 2nd drawn quadrant (math quadrant IV, 270-360)
    X = 0
    Y = -q
    count = 0
    while count <= sizeN:

        turtle.setpos(0, Y)
        turtle.pendown()
        turtle.goto(X, 0)
        turtle.penup()

        X += pixel
        Y += pixel       

        count += 1
            
    turtle.setpos(0, 0)

    # 3rd drawn quadrant (math quadrant III, 180-270)
    X = 0
    Y = -q
    count = 0
    
    while count <= sizeN:

        turtle.setpos(0, Y)
        turtle.pendown()
        turtle.goto(X, 0)
        turtle.penup()

        X -= pixel
        Y += pixel

        count += 1
        
    turtle.setpos(0, 0)
        
    # 4th drawn quadrant (math quadrant II, 90-180) 
    X = 0
    Y = q
    count = 0
    while count <= sizeN:

        turtle.setpos(0, Y)
        turtle.pendown()
        turtle.goto(X, 0)
        turtle.penup()

        X -= pixel
        Y -= pixel

        count += 1

    turtle.setpos(0, 0)

    print("Each quadrant is drawn with", count, "linear functions.")



