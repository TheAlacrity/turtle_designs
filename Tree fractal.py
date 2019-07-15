import turtle


def treeLeft(length,n):
    
    

    if length < (length/n) and (length/n) >= 8:
        turtle.pencolor(24, 6, 2)
        turtle.pensize(3)
        return
    

    elif length < (length/n) and (length/n) < 8:
        turtle.pencolor(15, 51, 0)
        turtle.pensize(1)
        return

        
        
    turtle.forward(length)
    turtle.left(45)
    treeLeft(length * 0.5,length/n)
    turtle.left(20)
    treeLeft(length * 0.5,length/n)
    turtle.right(75)
    treeLeft(length * 0.5,length/n)
    turtle.right(20)
    treeLeft(length * 0.5,length/n)
    turtle.left(30)
    turtle.backward(length)
    return


def treeRight(length,n):
    
    

    if length < (length/n) and length >=5:
        turtle.pencolor(48, 38, 33)
        turtle.pensize(3)
        return
    

    elif length < (length/n) and length < 5:
        turtle.pencolor(15, 51, 0)
        turtle.pensize(1)
        return

        
        
    turtle.forward(length)
    turtle.right(45)
    treeRight(length * 0.5,length/n)
    turtle.right(20)
    treeRight(length * 0.5,length/n)
    turtle.left(75)
    treeRight(length * 0.5,length/n)
    turtle.left(20)
    treeRight(length * 0.5,length/n)
    turtle.right(30)
    turtle.backward(length)
    return

turtle.colormode(255)

turtle.speed(10)

turtle.bgcolor(55,55,55)

turtle.pencolor(24, 6, 2)
turtle.pensize(12)

print(turtle.heading()) #
print(turtle.position())
turtle.left(90)
print(turtle.heading()) #
print(turtle.position())
turtle.backward(30)
print(turtle.heading())#
print(turtle.position())
treeLeft(200,4)
print(turtle.heading())#
print(turtle.position())


turtle.setposition(0,0)
turtle.setheading(90)
turtle.pencolor(24, 6, 2)
turtle.pensize(12)

#turtle.right(90)
turtle.backward(30)

treeRight(200,4)

