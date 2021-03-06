import turtle

from menu import colorMenu

def mathRedux():

    turtle.clear()

    a = turtle.Turtle()

    #from menu import colorMenu

    turtle.title ('Math Redux')
    a.ht() # hides turtle

    # (Red, Green, Blue), 0-255, of pen color and background
    #a.pencolor(255, 255, 255)    
    #turtle.bgcolor(0, 0, 30)
             
    a.penup()

    # size of star
    x = float(input("Size (pixels): "))

    myStart = (x/2, x/12)

    a.setpos(myStart)

    a.pendown()

    a.speed(10)
    
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


