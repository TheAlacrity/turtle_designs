
import turtle

from menu import colorMenu

def autoMath():

    turtle.clear()

    turtle.ht() # hides turtle

    turtle.colormode(255)
    turtle.bgcolor(200, 200, 100)
    turtle.pencolor(20, 20, 80)

    turtle.speed(10)

    pixel = 10

    size = 600
    
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



