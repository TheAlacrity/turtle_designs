import turtle
from menu import colorMenu

def autoMath():

#    turtle.clear()
    turtle.setup(2560, 1450)


    turtle.ht() # hides turtle

    turtle.colormode(255)
    turtle.bgcolor(70, 0, 0)
    turtle.pencolor(0, 0, 0)

    turtle.speed(12)

    pixel = 10

    size = 700
    
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
 


def autoMathRedux():


    #turtle.clear()

    turtle.colormode(255)
    turtle.bgcolor(40, 0, 0)
    turtle.pencolor(0, 0, 0)

    a = turtle.Turtle()

    #from menu import colorMenu

    turtle.title ('Auto Math Redux')
    turtle.ht() # hides turtle

    # (Red, Green, Blue), 0-255, of pen color and background
    #a.pencolor(255, 255, 255)    
    #turtle.bgcolor(0, 0, 30)
             
    a.penup()

    # size of star
    x = 1300

    myStart = (x/2, x/3.5)

    a.setpos(myStart)

    a.pendown()

    a.speed(11)
    
    # sets value for angle of each point
    n = 62

    pointCount = 0
    
    a.rt(180 - n)
    
    a.fd(x)

    pointCount += 1

    run = True

    while run == True:
        
        a.rt(180 - n)
    
        a.fd(x)

        pointCount += 1

        if a.distance(myStart) < 1.0:
            run = False

    print("This star has", pointCount, "points.") 


autoMath()
autoMathRedux()
