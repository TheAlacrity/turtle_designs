'''
Questions:

(1) ask about midterm Q with 3 correct answers

(2) Boolean variables only hold True or False

    play = True

    while(play):
    

    versus

    play = 3

    while play == 3:  Does this qualify as a boolean statement?



There is no better way to make me tune out then to say "no questions during lecture."

def m(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)

    print(str(slope))
    return


a += 1  #x1
b = 10  #y1

c = a + 1 #x2
d += 1  #y2

result = m(a, b, c, d)
'''



import turtle

def halfpipe():
    howMany = 0 #int(input("How many would you like? (Recommended 1-3):   "))

    rendition = 0
    b = 0
    d = 0
    f = 0
    h = 0
    #sm = 1
    #s = sm/4
    
    turtle.setpos(-450, 0)
               
    while rendition <= howMany:     
        # 1st drawn quadrant
        a = -450
        b += 450
        count = 0
        while count <= 45:
            #turtle.speed(s)
            turtle.setpos(-450, b)
            turtle.goto(a, 0)

            a += 10
            b -= 10
            #sm += 1
            
           #turtle.goto(a, 0)
            count += 1

        turtle.setpos(0, 0)
        turtle.setpos(-450, 0)
        #sm = 1
        # 2nd drawn quadrant
        c = -450
        d = -450
        count = 0
        while count <=45:

            turtle.setpos(-450, d)
            turtle.goto(c, 0)

            c += 10
            d += 10

            

            count += 1
            
        turtle.setpos(0, 0)
        turtle.setpos(450, 0)
        sm = 1
        # 3rd drawn quadrant
        e = 450
        f = -450
        count = 0
        while count <=45:

            turtle.setpos(450, f)
            turtle.goto(e, 0)

            

            e -= 10
            f += 10

            count += 1
        turtle.setpos(0, 0)
        turtle.setpos(450, 0)
        sm = 1
        # 4th drawn quadrant    
        g = 450
        h = 450
        count = 0
        while count <=45:

            turtle.setpos(450, h)
            turtle.goto(g, 0)

            g -= 10
            h -= 10

            count += 1
        turtle.setpos(0, 0)
        
        rendition += 1

        a += 450 #x
        #b += 400 
        c += 450 #x
        #d -= -400 
        e -= 450 #x
        #f -= -400
        g -= 450 #x
        # h += 400
                
halfpipe()
