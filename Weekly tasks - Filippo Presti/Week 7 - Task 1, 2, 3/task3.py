# REFERENCES

# Main idea for the task taken from website listed below
# https://www.geeksforgeeks.org/print-a-spirograph-using-turtle-in-python/
# Rainbow colour palette taken from picture listed below
# https://www.pinterest.co.uk/pin/564849978235605756/
# Ice-cream colour palette taken from picture listed below
# https://www.onyxcreative.com/blog/2020/9/popular-color-palettes-by-decade

#-------------------------------------------------------------------------------
# - Set up
# - Import turtle library
import turtle
t = turtle.Turtle()

# - Set speed of drawing to 20
t.speed(20)
# - Set background colour to light blue
t.screen.bgcolor("#B1E8F7")

#-------------------------------------------------------------------------------

#FIRST VERSION
# - Draw Spirograph using circle shapes

# - Calculate number of cicrles needed to complete the Spirograph
# - 360/10 = 36 circles

# Start commenting/un-commenting for FIRST VERSION here

#for i in range(0, 36):
#
#         # Hide the turtle/cursor while drawing
#         t.hideturtle()
#
#         # Draw a circle of chosen size, 100 here
#         t.circle(100)
#
#         # Move 10 pixels right to draw the following circle
#         t.right(10)
#
#turtle.done()

# stop commenting/un-commenting for FIRST VERDION here

#-------------------------------------------------------------------------------

# SECOND VERSION
# - Draw Spirograph using circles with rainbow colour palette

# - Calculate number of repetitions with colour palette of 6 different given colours
# - 36 circles / 6 colours = 6 repetitions

# Start commenting/un-commenting for SECOND VERSION here

# for i in range(0, 6):
#
#     for colour in ('#DB3838', '#F9A228', '#FECC2F', '#B2C225', '#40A4D8', '#A363D9'):
#         t.color(colour)
#
#         # Draw a circle of chosen size 100
#         t.circle(100)
#
#         # Move 10 pixels left to draw the following circle
#         t.left(10)
#
# # Hide turtle/cursor once the drawing is completed
# t.hideturtle()
# turtle.done()

# stop commenting/un-commenting for SECOND VERSION here

#-------------------------------------------------------------------------------

# THIRD VERSION
# - Draw Spirograph using squares with ice-cream colour palette

# - Calculate number of squares needed to complete the Spirograph
# - 360/20 = 18 squares
# - Calculate number of repetitions with colour palette of 6 different given colours
# - 18 squares / 6 colours = 3 repetitions

# Start commenting/un-commenting for THIRD VERSION here
t.screen.bgcolor("black")
for i in range(0, 3):

    for colour in ('#E2D2DF', '#F6CCD0', '#BBDCCB', '#B4DDE3', '#FDEEB3', '#D9CBC2'):
        t.color(colour)

        # Draw a square of chosen sides size 250
        t.pensize(2)
        t.forward(250)
        t.left(90)
        t.forward(250)
        t.left(90)
        t.forward(250)
        t.left(90)
        t.forward(250)
        t.left(90)
        # Move 10 pixels left to draw the following circle
        t.left(20)

# Hide turtle/cursor once the drawing is completed
t.hideturtle()
turtle.done()

# Stop commenting/un-commenting for THIRD VERSION here

#-------------------------------------------------------------------------------

# FOURTH VERSION
# - Draw Spirograph using triangles with ice-cream colour palette

# Start commenting/un-commenting for FOURTH VERSION here
# t.screen.bgcolor("white")
# for i in range(0, 3):
#
#     for colour in ('#E2D2DF', '#F6CCD0', '#BBDCCB', '#B4DDE3', '#FDEEB3', '#D9CBC2'):
#         t.color(colour)
#
#         # Draw a triancle of chosen sides size 250
#         t.pensize(2)
#         t.forward(250)
#         t.right(120)
#         t.forward(250)
#         t.right(120)
#         t.forward(250)
#         t.right(120)
#         t.forward(250)
#         t.right(120)
#         # Move 10 pixels right to draw the following circle
#         t.right(20)
#
# # Hide turtle/cursor once the drawing is completed
# t.hideturtle()
# turtle.done()

# Stop commenting/un-commenting for FOURTH VERSION here

#-------------------------------------------------------------------------------

# FIFTH VERSION (just for fun)
# code from youtube tutorial: https://www.youtube.com/watch?v=ogsRn1XSy5c
# - Draw Spirograph using squares with constant incrementation

# Start commenting/un-commenting for FIFTH VERSION here

#t.screen.bgcolor("black")
#colours = ['pink', 'violet']
#for i in range(0, 400):
#
#         t.forward(i)
#         t.right(89)
#         t.pencolor(colours[i%2])
#
# # Hide turtle/cursor once the drawing is completed
#t.hideturtle()
#turtle.done()

# Stop commenting/un-commenting for FIFTH VERSION here
