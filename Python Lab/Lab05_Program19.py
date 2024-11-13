#                                                                               22-10-2024
#                                                                            LAB SESSION 4:
#                                                                   CONTAINER TYPES IN PYTHON – LIST , SET
# 
#                                                                             Program 19

#Generate two tuples to represent two distinct points in space. (Three dimensional geometry). Determine the Euclidean distance between the two.

import math
A= tuple([float(x) for x in input("Enter coordinates of Point 1 (x y z): ").split()])
B= tuple([float(x) for x in input("Enter coordinates of Point 2 (x y z): ").split()])
print(A)
print(B)
distance = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)
print("Distance:",distance)
