import turtle

def colorMenu():

    option = input("\nOptions:\n(1) Black pen on white background \n(2) White pen on black background \n" +
                   "(3) White pen on blue background\n(4) White pen on red background\n(5) White pen on purple"
                   + " background\n(6) Custom\n\nOption number: ")

    a = turtle.Turtle()

    a.ht() # hides turtle 

    turtle.colormode(255)

    if option == '1':
        turtle.bgcolor(255, 255, 255) # white
        turtle.pencolor(0, 0, 0) # black

    elif option == '2':  
        turtle.bgcolor(0, 0, 0) # black
        turtle.pencolor(255, 255, 255) # white

    elif option == '3':  
        turtle.bgcolor(0, 0, 40) # blue
        turtle.pencolor(255, 255, 255) # white

    elif option == '4':
        turtle.bgcolor(40, 0, 0) # red
        turtle.pencolor(255, 255, 255) # white

    elif option == '5': 
        turtle.bgcolor(40, 0, 40) # purple
        turtle.pencolor(255, 255, 255) # white

    elif option == '6':

        bgR = int(input("Background red value (0-255): "))
        bgG = int(input("Background green value (0-255): "))
        bgB = int(input("Background blue value (0-255): "))

        bgTup = (bgR, bgG, bgB)

        penR = int(input("Pen red value (0-255): "))
        penG = int(input("Pen green value (0-255): "))
        penB = int(input("Pen blue value (0-255): "))

        penTup = (penR, penG, penB)
        
        turtle.bgcolor(bgTup)
        turtle.pencolor(penTup)
