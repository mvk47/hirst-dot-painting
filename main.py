import colorgram
from turtle import *
import random
screen=Screen()
screen.colormode(255)
colors = colorgram.extract('heist.jpg', 30)
list1 = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    list1.append(new_color)

color_list=list1[4:]
print(color_list)

timmy = Turtle()
def draw(space,x):
    for i in range(x):
        for j in range(x):
            num=random.randint(1,25)
            timmy.dot(10, color_list[num])
            timmy.forward(space)
        timmy.backward(space*x)

        timmy.right(90)
        timmy.forward(space)
        timmy.left(90)
timmy.penup()
draw(20,20)
screen.exitonclick()
