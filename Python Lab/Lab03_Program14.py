#                                                                           Program 14

# Write a python script to find the number of occurrences of a particular character present in the given string using a loop.
#  (Don’t use string methods).

s=str(input("Enter string:"))
a=str(input("Enter character:"))
count=0
for i in s:
    if(i==a):
        count=count+1
print("Number of occurence is:",count)




