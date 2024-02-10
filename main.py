import colorgram
import turtle as t
import random

colors = colorgram.extract('hirst-painting.jpg', 10)

rgb_tuple_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188),
                  (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_tuple_list.append(color_tuple)
#
# print(rgb_tuple_list)

rex = t.Turtle()
rex.shape('arrow')
rex.width(20)
rex.hideturtle()

t.colormode(255)
screen = t.Screen()
screen.bgcolor('black')

rex.setheading(225)
rex.penup()
rex.forward(330)
rex.setheading(0)
rex.pendown()


def draw_a_line(number):
    for digit in range(10):
        rex.pencolor(random.choice(rgb_tuple_list))
        rex.forward(0)
        rex.penup()
        rex.forward(50)
        rex.pendown()
    if number % 2 == 0:
        rex.penup()
        rex.left(90)
        rex.forward(50)
        rex.left(90)
        rex.forward(50)
        rex.pendown()
    else:
        rex.penup()
        rex.right(90)
        rex.forward(50)
        rex.right(90)
        rex.forward(50)
        rex.pendown()


for num in range(10):
    draw_a_line(num)
rex.color('black')

screen.mainloop()
