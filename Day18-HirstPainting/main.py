import random
import turtle as t

import colorgram


def get_colors():
    colors = colorgram.extract('colors.jpg', 20)

    color_list = []

    for col in colors:
        color_tuple = {col.rgb.r, col.rgb.g, col.rgb.b}
        color_list.append(color_tuple)
    return color_list
   
def get_color(colors):
    choice = random.choice(colors)
    test = tuple(choice)
    return tuple(choice)

def draw_circle(x, y):
    tim = t.Turtle()
    t.colormode(255)
    
    tim.speed("fastest")
    tim.penup()
    tim.color(get_color(colors))
    tim.setpos(x, y) 
    tim.shape("circle")
    tim.pendown()

def update_coords(coords, max_x, distance):
    if coords[0] == (distance * max_x) - distance:
        coords[1] += distance
        coords[0] = 0
    else:
        coords[0] += distance
    return coords
    
colors = get_colors()

coords = [0, 0]
size_x = 10
distance_between = 50
number_of_dots = 100

for _ in range(number_of_dots):
    draw_circle(coords[0],coords[1])
    
    update_coords(coords, size_x, distance_between)
    
screen = t.Screen()
screen.exitonclick()