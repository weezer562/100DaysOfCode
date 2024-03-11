import random
import turtle as t

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)    

def draw_spirogrpah(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
    
    
tim = t.Turtle()
t.colormode(255)

# screen.colormode(255)

#=========Draw all Shapes==========
# for shape in range(3, 11):
#     tim.pencolor(random_color())
#     draw_shape(shape)
 
# ========Turtle initial===========
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# =======Turtle Square ============
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# tim.left(90)
 
#========Turtle Dash lines=========
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
    
#=======Random Turtle Path ========
# for _ in range(200):
#     tim.pencolor(random_color()) 
#     tim.pensize(15)
#     tim.speed("fastest")
    
#     distance = random.randint(10,50)
#     tim.forward(distance)
    
#     directions = [0, 90, 180, 270]
#     direction = random.choice(directions)
    
#     tim.setheading(direction)

#==========Spirograph===============
draw_spirogrpah(5)

screen = t.Screen()
screen.exitonclick()