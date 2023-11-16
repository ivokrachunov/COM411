'''1
import matplotlib.pyplot as plt

def display_line(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel('x_values')
    plt.ylabellot('y_values')
    plt.title('Line Plot')
    plt.show

def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)
# Call the run_task1 function to
'''

'''1 secound way
import turtle

def display_line(x_values, y_values):
    turtle.penup()
    turtle.goto(x_values[0], y_values[0])
    turtle.pendown()

    for x, y in zip(x_values, y_values):
        turtle.goto(x, y)
        turtle.dot()

    turtle.done()

def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)

# Call the run_task1 function to display the line
run_task1()
'''
'''
import turtle


def draw_square(x, y, size, color, linestyle, marker):
    turtle.penup()
    turtle.goto(x[0] * size, y[0] * size)
    turtle.pendown()

    turtle.color(color)
    turtle.pendown()
    turtle.pensize(2)

    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.penup()
    turtle.goto(x[0] * size, y[0] * size)
    turtle.pendown()


def small():
    draw_square([1, 2, 2, 1], [1, 1, 2, 2], 30, 'red', 'dotted', 'circle')


def medium():
    draw_square([0, 3, 3, 0], [0, 0, 3, 3], 40, 'green', 'dashed', 'square')


def large():
    draw_square([-1, 4, 4, -1], [-1, -1, 4, 4], 50, 'blue', 'solid', 'pentagon')


# Set up the turtle screen
turtle.speed(2)
turtle.hideturtle()

# Call the functions to draw the squares
small()
medium()
large()

# Keep the window open
turtle.done()
'''

