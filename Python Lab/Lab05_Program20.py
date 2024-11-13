#                                                                             Program 20

#Enter the coordinates of two points on the cartesian plane (take user input using comprehension). Find the equation of
# the straight line passing through these points.
#Hint: Eqn is (x-x1) = ((x1-x2)/(y1-y2)) (y-y1)

x1, y1 = [float(x) for x in input("Enter coordinates of Point 1 (x y): ").split()]
x2, y2 = [float(x) for x in input("Enter coordinates of Point 2 (x y): ").split()]
if y2 - y1 == 0:
    print("Infinite slope. Vertical line equation: x =", x1)
elif x2 - x1 == 0:
    print("Zero slope. Horizontal line equation: y =", y1)
else:
    m = (y2 - y1) / (x2 - x1)
    print(f" Slope (m) = {m}")
    print(f"Equation: (y - {y1}) = {m}(x - {x1})")
    b = y1 - m * x1
    print(f"Equation (slope-intercept form): y = {m}x + {b}")

