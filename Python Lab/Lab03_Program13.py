#                                                                           Program 13

# Write a python script to check whether all the characters present in a string are alphanumeric 
# (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.

s=str(input("Enter your string:"))
b=True
for i in s:
    if((ord(i)<=57 and ord(i)>=48) or (ord(i)<=90 and ord(i)>=65) or (ord(i)<=122 and ord(i)>=97)):
        continue
    else:
        b=False
        break
if(b==True):
    print("TRUE")
else:
   print("FALSE")
