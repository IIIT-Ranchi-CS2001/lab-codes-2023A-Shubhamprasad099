#                                                                              20-08-2024
#                                                                         Program 2
# #Write a python program to find
# a) area & perimeter when all three sides are given(take users input)
# b) find all 3 angles of the above traingle
import math
a=float(input("Enter 1st side "))
b=float(input("Enter 2nd side "))
c=float(input("Enter 3rd side "))
print("Perimeter = ",a+b+c)
s=(a+b+c)/2
print("Area =", math.sqrt(s*(s-a)*(s-b)*(s-c)))
x= math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
y= math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
z= math.degrees(math.acos((b**2+a**2-c**2)/(2*a*b)))
print("Angles are",x ,y, z)

