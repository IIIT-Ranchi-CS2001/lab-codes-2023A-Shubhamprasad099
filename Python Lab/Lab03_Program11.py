#                                                                           Program 11

# Write a python script to print the first n terms of the Fibonacci series using while loop

n=int(input("Enter a number: "))
a=0
b=1
print(a,b, end=" ")
i=0
c=0
while(i<=n-2):
    c=a+b
    print(c, end=" ")
    a=b
    b=c
    i=i+1
