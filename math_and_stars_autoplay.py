import tkinter as tk
import turtle

def math():

    WIDTH, HEIGHT = 2560, 1440

    root = tk.Tk()

    canvas = turtle.ScrolledCanvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor('black')
    
    t = turtle.RawTurtle(screen, visible=False)


    # canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)


    # turtle = RawTurtle(screen, visible=False)
    t.speed('fastest')
    # t.color('blue')
    shape_color = 'blue'
    t.pencolor(shape_color)

    box_width = 10

    scope = 700 # max height and width of one quadrant
    
    q = (scope * box_width) / 10

    lines_to_draw = scope / 10


    # 1st drawn quadrant (math quadrant I, 0-90)
    X = 0
    Y = q
    total_lines = 0
    count = 0
    while count <= lines_to_draw:

        t.setpos(0, Y)
        t.pendown()
        t.goto(X, 0)
        t.penup()

        X += box_width
        Y -= box_width
                 
        count += 1
        total_lines += 1

    t.setpos(0, 0)

    # 2nd drawn quadrant (math quadrant IV, 270-360)
    X = 0
    Y = -q
    total_lines -= 1 # accounts for redrawing of positive x axis line
    count = 0
    while count <= lines_to_draw:

        t.setpos(0, Y)
        t.pendown()
        t.goto(X, 0)
        t.penup()

        X += box_width
        Y += box_width       

        count += 1
        total_lines += 1
            
    t.setpos(0, 0)

    # # 3rd drawn quadrant (math quadrant III, 180-270)
    X = 0
    Y = -q
    total_lines -= 1 # accounts for redrawing of negative y axis line
    count = 0
    
    while count <= lines_to_draw:

        t.setpos(0, Y)
        t.pendown()
        t.goto(X, 0)
        t.penup()

        X -= box_width
        Y += box_width

        count += 1
        total_lines += 1
        
    t.setpos(0, 0)
        
    # # 4th drawn quadrant (math quadrant II, 90-180) 
    X = 0
    Y = q
    count = 0
    while count <= lines_to_draw:

        t.setpos(0, Y)
        t.pendown()
        t.goto(X, 0)
        t.penup()

        X -= box_width
        Y -= box_width

        count += 1
        total_lines += 1

    t.setpos(0, 0)

    total_lines -= 2 # accounts for redrawing of negative x and positive y axis line


    t.pencolor('white')

    arg = f"The {shape_color} shape is drawn with {total_lines} linear functions"
    t.write(arg, move=True, align="left", font=("Arial", 30, "normal"))

    screen.mainloop()

math()