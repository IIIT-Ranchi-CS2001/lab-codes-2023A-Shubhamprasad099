
 #                                                         Program 8
# Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)
# Hint: find the discriminant d= b2 − 4ac
# If d = 0, the equation has one real repeated root (both roots are the same: 
# R1= R2 = -b/(2a)
# If d > 0, the equation has two distinct real roots.
# 	R1= (-b + sqrt(d))/2a
# R2= (-b - sqrt(d))/2a
# If d < 0, the equation has two complex roots.
# real_part = -b / (2 * a) 
# imaginary_part = math.sqrt(-discriminant) / (2 * a)

import math
a=int(input("Enter the Coefficient a:"))
b=int(input("Enter the Coefficient b:"))
c=int(input("Enter the Coefficient c:"))
d=b**2-4*a*c
if(d==0):
    print("Both roots are same:")
    print(-b/2*a)
elif(d>0):
    print("First root:",(-b + math.sqrt(d))/2*a)
    print("Second root:",(-b-math.sqrt(d))/2*a)
else:
    print(" Real Part is",-b/(2*a))
    print(" Imaginary Part:",math.sqrt(-d)/2*a)
    