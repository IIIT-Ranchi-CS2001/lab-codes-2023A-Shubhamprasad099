#                                                                           Program 12

#Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.

n=int(input("ENter number:"))
m=int(input("Enter limit:"))
i=1
while(i<=m):
    print(n, "* ",i," =" ,n*i)
    i=i+1

