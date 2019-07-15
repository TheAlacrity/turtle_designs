import turtle

from Eighth_Grade_Math_turtle_code_v3 import eighthGradeMath

from menu import colorMenu

from Stars import star

from autoMath import autoMath

from autoMathRedux import autoMathRedux

def designChoice():

#    colorMenu()

    again = 'y'

    while again == 'y':
    
        print("\n(1) EighthGradeMath")
        print("(2) STAR")
        print("(3) CLEAR")
        print("(4) MENU\n")
        print("(5) autoMath")
        print("(6) autoMathRedux")
        print("QUIT")


        choice = input("Choice number: ") 

        if choice == 'EighthGradeMath' or choice == '1' :
            eighthGradeMath()         

        elif choice == 'STAR' or choice == '2':
            star()         

        elif choice == 'CLEAR' or choice == '3':
            turtle.clear()

        elif choice == 'MENU' or choice == '4':
            colorMenu()

        elif choice == 'autoMath' or choice == '5':
            autoMath()

        elif choice == 'autoMathRedux' or choice =='6':
            autoMathRedux()

        elif choice == 'autoMathPattern' or choice =='7':
            autoMathPattern()

        elif choice == 'QUIT':# or choice == '5':
            raise SystemExit

        else:
            print("Invalid Selection!")

        pause = input("\nPress Enter to continue.\n")

designChoice()
