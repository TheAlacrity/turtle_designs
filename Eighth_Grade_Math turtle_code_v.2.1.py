
import turtle

def eighthGradeMath():

    faster = int(input("How fast? 1-10, 1 is slow, 10 is fast:  "))

    turtle.speed(faster)

    size = float(input("What size would you like? (Recommended 45):  "))

    pixel = int(input("How detailed would you like it? (Pixel separation; " +
         "10 is recommended. Smaller numbers give more detail.):  "))
    
    q = size * 10
    bX = 0
    d = 0
    f = 0
    h = 0
                  

    # 1st drawn quadrant (math quadrant I, 0-90)
    aX = 0
    bY = q
    count = 0
    while count <= size:

        turtle.setpos(0, bY)
        turtle.goto(aX, 0)

        aX += pixel
        bY -= pixel
                 
        count += 1

    turtle.setpos(0, 0)

    # 2nd drawn quadrant (math quadrant IV, 270-360)
    cX = 0
    dY = -q
    count = 0
    while count <= size:

        turtle.setpos(0, dY)
        turtle.goto(cX, 0)

        cX += pixel
        dY += pixel       

        count += 1
            
    turtle.setpos(0, 0)

    # 3rd drawn quadrant (math quadrant III, 180-270)
    eX = 0
    fY = -q
    count = 0
    
    while count <= size:

        turtle.setpos(0, fY)
        turtle.goto(eX, 0)   

        eX -= pixel
        fY += pixel

        count += 1
        
    turtle.setpos(0, 0)
        
    # 4th drawn quadrant (math quadrant II, 90-180) 
    gX = 0
    hY = q
    count = 0
    while count <= size:

        turtle.setpos(0, hY)
        turtle.goto(gX, 0)

        gX -= pixel
        hY -= pixel

        count += 1
        
    turtle.setpos(0, 0)


reset = 'y'

while reset == 'y' or 'Y':                

    eighthGradeMath()

    reset = input("Clear the screen? Hit y for yes and press Enter:  ")

    if reset == 'y' or reset == 'Y':
        turtle.reset()

raise SystemExit








