#                                                                            10-09-2024
#                                                                            LAB SESSION 3:
#                                                                        LOOP CONTROL INSTRUCTIONS
# 
#                                                                             Program 9
#
# Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop
# Number    	Square
# 1              	1
# 2               	4
# …		            …
# n		            n

n=int(input("Enter a number: "))
i=1
print("NUMBER      SQUARE")
while(i<=n):
    print("  ",i,"        ",i**2)
    i=i+1
