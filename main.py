from turtle import Turtle,Screen
import random
#create paint object
paint=Turtle()
paint.hideturtle()
#color list
color_list=[(202,164, 189), (238, 240, 245), (150, 75, 49), (223, 201, 135), (198, 116, 165), (144, 55, 79)]

# Function to convert RGB tuple to hex color
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
#starting position
def position():
 paint.penup()
 x=-200
 y=0
 paint.goto(x,y)
 paint.pendown()


def draw(paint,color_list):
    for i in range(10):
         chosen_color=random.choice(color_list)
         paint.color(rgb_to_hex(chosen_color))
         paint.dot(15)
         paint.penup()
         paint.fd(35)

position()
draw(paint,color_list)














screen = Screen()
screen.exitonclick()