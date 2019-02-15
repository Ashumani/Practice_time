#A number (N) of lines (extending to infinity) in both directions are drawn on a plane. The lines are specified by the angle (positive or negative) made with the x axis (in degrees). It may be assumed that the different lines are not coincident (they do not overlap each other). The objective is to determine the number of parallelograms in the plane formed by these lines.

#If the lines are given with an angle of 10, 70, 30 and 30, the figure looks like th


# import turtle



# def draw_triangle():
#      turtle.setup(700, 500)
#      window = turtle.Screen()
#      window.bgcolor("green")  # background color
#      tom = turtle.Turtle()
#      tom.degrees(100,200)
#      # tom.left(120)
#      # tom.forward(100)
#      # tom.left(120)
#      # tom.forward(100)
#      window.exitonclick()  # to exit
#
#
# draw_triangle()

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

x = np.array([1,2,3,4])
y = np.array([1,2,8,12])
x_smooth = np.linspace(x.min(), x.max(), 400)
y_smooth = spline(x,y,x_smooth)
plt.plot(x_smooth,y_smooth)
plt.show()