
import turtle

from menu import colorMenu

def autoMathPattern():

    turtle.ht() # hides turtle

    turtle.colormode(255) # sets to RGB mode
    turtle.bgcolor(20, 20, 125)
    turtle.pencolor(0, 0, 0)

    turtle.speed(2)

    pixel = 15

    size = 100
    


#    sizeN = size / 10

    # 1st drawn quadrant (math quadrant I, 0-90)


    times = 0

    count = 0

    originX = 0
    originY = 0

    while times <= 4:

        X = 0
        Y = (size * pixel) / 10
        
        if count <= (size / 10):

            turtle.setpos(originX, Y)
            turtle.pendown()
            turtle.goto(X, originY)
            turtle.penup()

            X += pixel
            Y -= pixel
                 
            count += 1

            #break

        originX += ((size * pixel) / 10)

        turtle.setpos(originX, originY)

        originY -= size

        Y -= ((size * pixel) / 10)

        times += 1
        
autoMathPattern()

'''
#        count = 0
        

        while count <= (sizeN):

            turtle.setpos(originX, Y)
            turtle.pendown()
            turtle.goto(X, originY)
            turtle.penup()

            X += pixel
            Y -= pixel
                 
            count += 1

        turtle.setpos(X, Y)

        times += 1
        sizeA += size

        originX += size
        originY -= size

        turtle.setpos(originX, originY)




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

'''

