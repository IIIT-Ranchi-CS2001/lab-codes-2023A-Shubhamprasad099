
#                                                                           Program 10

#Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.

n=int(input("Enter a number: "))
i=n
s=0
while(i>0):
    s=s+(i%10)
    i=i//10
print("Sum is:", s)
