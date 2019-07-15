
import turtle

def eighthGradeMath():

    faster = int(input("How fast? 1-10, 1 is slow, 10 is fast:  "))

    turtle.speed(faster)

    size = float(input("What size would you like? (Recommended 45):  "))

    pixel = int(input("How detailed would you like it? (Pixel separation; " +
         "10 is recommended. Smaller numbers give more detail.):  "))
    
    x = size * 10
    b = 0
    d = 0
    f = 0
    h = 0
                  

    # 1st drawn quadrant (math quadrant I, 0-90)
    a = 0
    b += x
    count = 0
    while count <= size:

        turtle.setpos(0, b)
        turtle.goto(a, 0)

        a += pixel
        b -= pixel
                 
        count += 1

    turtle.setpos(0, 0)

    # 2nd drawn quadrant (math quadrant IV, 270-360)
    c = 0
    d = -x
    count = 0
    while count <= size:

        turtle.setpos(0, d)
        turtle.goto(c, 0)

        c += pixel
        d += pixel       

        count += 1
            
    turtle.setpos(0, 0)

    # 3rd drawn quadrant (math quadrant III, 180-270)
    e = 0
    f = -x
    count = 0
    
    while count <= size:

        turtle.setpos(0, f)
        turtle.goto(e, 0)   

        e -= pixel
        f += pixel

        count += 1
        
    turtle.setpos(0, 0)
        
    # 4th drawn quadrant (math quadrant II, 90-180) 
    g = 0
    h = x
    count = 0
    while count <= size:

        turtle.setpos(0, h)
        turtle.goto(g, 0)

        g -= pixel
        h -= pixel

        count += 1
        
    turtle.setpos(0, 0)


again = 'y'

while again == 'y' or 'Y':                

    eighthGradeMath()

    reset = input("Clear the screen? Hit y for yes and press Enter:  ")

    if reset == 'y' or reset == 'Y':
        turtle.reset()








