#                                                       Program 6
#Write a python script to enter any string at run time and check whether it is a palindrome or not
a= str(input("Enter the string with 1st letter small:"))
if(a==a[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")
