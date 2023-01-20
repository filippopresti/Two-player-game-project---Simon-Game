#turtle is a built-in module that comes with python itself
import turtle

#Not sure what the task involved
#function implemented in order to draw polygons having only the number of sides
t = turtle.Turtle()

def draw_polygon(side_length, sides):
    #x = (sides - 2) * 180/sides
radius
    for i in range(0, sides):
        t.forward(side_length)
        #t.right(180-x);
        t.right(360/sides);

    turtle.done()

#draw_square(100)
draw_polygon(100, 5)
