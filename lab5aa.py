"""Module implementing functions for various functions utelizing turtle to create different shapes
completed by Augustin Au on 2024-10-07 fo DS-1043"""

import math
import turtle
from stack import print_frame
Number =int|float
def square(t):
    """function prints a square"""
    for x in range(4):
        turt.fd(50)
        turt.lt(90)
        print_frame("square", locals(), step=False)


def spacing_right(length: Number):
    turt.up()
    turt.fd(length)
    turt.down()


def spacing_up (length: Number):
    turt.up()
    turt.lt(90)
    turt.fd (100)
    turt.down()

def generalize_square(length: Number):
    """function returns a square when given the length number"""
    for x in range(4):
        turt.fd(length)
        turt.lt(90)


def polygon(length: Number, n: Number):
    """Function returns a polygon when given a length and number of sides"""
    for x in range(round(n)):
        turt.fd(length)
        turt.lt(180-((n-2)*180)/n)
        print_frame("polygon", locals(), step=False)

def circle( radius: Number):
    """Function returns a circle when given a radius"""
    cirumference = 2* math.pi *radius
    polygon(cirumference/50, 50)
    print_frame("circle", locals(), step=False)


def arc (angle: Number, radius: Number, ):
    """Function returns an arc when given an angle and radius"""
    percent = angle/360
    circumference = 2 * math.pi * radius
    for x in (range(round(percent*360))):
        turt.fd(circumference/360)
        turt.lt(180-((360-2)*180)/360)

def flower (petal_number: Number, radius: Number):
    """Function returns a flower when given the number of petals and a petal radius"""
    if petal_number%2==0:
        petal_number=petal_number*2
        radius=radius*2
    else:
        petal_number=petal_number
    for x in range(petal_number):
        arc(360/petal_number,radius)
        turt.lt(180-(360/petal_number))
        arc(360/petal_number,radius)
        turt.rt(180-(360/petal_number))

def pie(slice_number: Number, slice_length: Number):
    """Function returns a pie when given a slice number and length"""
    interior_angle = (360/slice_number)
    exterior_angle = ((180-(interior_angle))/2)
    for x in range(slice_number):
        turt.fd(slice_length)
        turt.lt(180-exterior_angle)
        turt.fd(slice_length*(math.sin((math.pi/180)*interior_angle)/math.sin((math.pi/180)*exterior_angle)))
        turt.lt(180-exterior_angle)
        turt.fd(slice_length)
        turt.lt(180)

def letter_A(height: Number):
    """Function prints an A when given a height"""
    turt.rt(30)
    turt.fd(height)
    turt.rt(120)
    turt.fd(height/2)
    turt.rt(120)
    turt.fd(height/2)
    turt.rt(180)
    turt.fd(height/2)
    turt.rt(60)
    turt.fd(height/2)



def letter_B(height: Number):
    """Function prints a B when given a height"""
    arc(180,height/4)
    turt.rt(180)
    arc(180, height/4)
    turt.lt(90)
    turt.fd(height)

def letter_C(height: Number):
    """Function prints an C when given a height"""
    arc(180, height/2)

def letter_D (height: Number):
    """Function prints a D when given a height"""
    arc(180, height/2)
    turt.lt(90)
    turt.fd(height)

def letter_E (height: Number):
    """Function prints an E when given a height"""
    turt.fd(height)
    turt.rt(90)
    turt.fd(height/2)
    turt.rt(180)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)
    turt.rt(180)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)

def letter_F (height: Number):
    """Function prints an F when given a height"""
    turt.fd(height)
    turt.rt(90)
    turt.fd(height/2)
    turt.rt(180)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)

def letter_G (height: Number):
    """Function prints a G when given a height"""
    arc(270, height/2)
    turt.lt(90)
    turt.fd(height/6)
    turt.lt(180)
    turt.fd(height/3)

def letter_H (height: Number):
    """Function prints an H when given a height"""
    turt.fd(height)
    turt.rt(180)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)
    turt.lt(90)
    turt.fd(height/2)
    turt.rt(180)
    turt.fd(height)

def letter_I (height: Number):
    """Function prints an I when given a height"""
    turt.fd(height/3)
    turt.rt(180)
    turt.fd(height/6)
    turt.rt(90)
    turt.fd(height)
    turt.rt(90)
    turt.fd(height/6)
    turt.rt(180)
    turt.fd(height/3)

def letter_J (height: Number):
    """Function prints a J when given a height"""
    arc(180,height/3)
    turt.fd(height)

def letter_K (height: Number):
    """Function prints a K when given a height"""
    turt.fd(height)
    turt.rt(180)
    turt.fd(height/2)
    turt.lt(135)
    turt.fd(math.sqrt(((height/2)**2)+((height/2)**2)))
    turt.rt(180)
    turt.fd(math.sqrt(((height/2)**2)+((height/2)**2)))
    turt.rt(270)
    turt.fd(math.sqrt(((height/2)**2)+((height/2)**2)))

def letter_L (height: Number):
    """Function prints an L when given a height"""
    turt.fd(height)
    turt.rt(180)
    turt.fd(height)
    turt.lt(90)
    turt.fd(height/3)

def letter_M (height: Number):
    """Function prints an M when given a height"""
    turt.fd(height)
    turt.rt(135)
    turt.fd(height/3)
    turt.lt(90)
    turt.fd(height/3)
    turt.rt(135)
    turt.fd(height)

def letter_N (height: Number):
    """Function prints an N when given a height"""
    turt.fd(height)
    turt.rt(135)
    turt.fd(math.sqrt(((height)**2)+((height)**2)))
    turt.lt(135)
    turt.fd(height)

def letter_O (height: Number):
    """Function prints an O when given a height"""
    circle(height/2)

def letter_P (height: Number):
    """Function prints a P when given a height"""
    arc(180, height / 4)
    turt.rt(270)
    turt.fd(height)

def letter_Q (height: Number):
    """Function prints a Q when given a height"""
    circle(height/2)
    turt.lt(90)
    turt.fd(height/8)
    turt.lt(180)
    turt.fd(height/4)

def letter_R (height: Number):
    """Function prints an R when given a height"""
    arc(180, height / 4)
    turt.rt(270)
    turt.fd(height)
    turt.rt(180)
    turt.fd(height/2)
    turt.rt(135)
    turt.fd(math.sqrt(((height/2)**2)+((height/2)**2)))

def letter_S (height: Number):
    """Function prints a S when given a height"""
    arc(180, height/4)
    turt.rt(180)
    turt.up()
    arc(150, height/4)
    turt.down()
    arc(210, height/4)

def letter_T (height: Number):
    """Function prints a T when given a height"""
    turt.fd(height)
    turt.rt(90)
    turt.fd(height/3)
    turt.rt(180)
    turt.fd((2/3)*height)

def letter_U (height: Number):
    """Function prints a U when given a height"""
    turt.fd(height)
    arc(180,height/3)
    turt.fd(height)

def letter_V (height: Number):
    """Function prints a V when given a height"""
    turt.fd(height)
    turt.lt(135)
    turt.fd(height)

def letter_W (height: Number):
    """Function prints a W when given a height"""
    turt.fd(height)
    turt.lt(135)
    turt.fd(height)
    turt.rt(135)
    turt.fd(height)
    turt.lt(135)
    turt.fd(height)

def letter_X (height: Number):
    """Function prints an X when given a height"""
    turt.fd (height)
    turt.lt(180)
    turt.fd(height/2)
    turt.rt(90)
    turt.fd(height/2)
    turt.rt(180)
    turt.fd(height)

def letter_Y (height: Number):
    """Function prints a Y when given a height"""
    turt.fd(math.sqrt(((height/2)**2)+((height/2)**2)))
    turt.lt(135)
    turt.fd(math.sqrt(((height/2)**2)+((height/2)**2)))
    turt.lt(180)
    turt.fd(math.sqrt(((height / 2) ** 2) + ((height / 2) ** 2)))
    turt.lt(45/2)
    turt.fd(height/2)

def letter_Z (height: Number):
    """Function prints a Z when given a height"""
    turt.fd(height)
    turt.rt(135)
    turt.fd(math.sqrt(((height)**2)+((height)**2)))
    turt.lt(135)
    turt.fd(height)




if __name__ == "__main__":
    turt = turtle.Turtle()
    turt.speed(10)
    print_frame("__main__", globals(), step=False)

    square(turt)
    flower(6,30)

    generalize_square(30)
    spacing_right(100)
    polygon(10,5)
    spacing_right(100)
    circle(30)
    spacing_up(100)
    pie(8,50)
    turt.up()
    turt.lt(90)
    turt.fd(500)
    turt.down()
    turt.rt(90)
    letter_A(50)
    turt.lt(60)
    turt.up()
    turt.fd(30)
    turt.lt(90)
    turt.fd(40)
    turt.rt(180)

    turt.down()
    letter_U(30)
    turt.up()
    turt.rt(180)
    turt.fd(50)
    turt.lt(90)
    turt.fd(40)
    turt.lt(90)
    turt.fd(50)
    turt.lt(90)
    turt.down()
    letter_G(40)
    turt.up()
    turt.fd(25)
    turt.lt(90)
    turt.fd(20)
    turt.rt(180)
    turt.down()
    letter_U(30)
    turt.up()
    turt.rt(90)
    turt.fd(30)
    turt.rt(180)
    turt.down()
    letter_S(40)
    turt.up()
    turt.rt(180)
    turt.fd(30)
    turt.rt(90)
    turt.fd(20)
    turt.rt(180)
    turt.down()
    letter_T(35)
    turt.up()
    turt.rt(180)
    turt.fd(50)
    turt.rt(90)
    turt.fd(40)
    turt.lt(90)
    turt.down()
    letter_I(40)
    turt.up()
    turt.lt(180)
    turt.fd(40)
    turt.rt(90)
    turt.fd(40)
    turt.rt(180)
    turt.down()
    letter_N(40)



    turt.screen.mainloop()

# Calls to functions written for "Generalizing Functions"
# BB.
#123





