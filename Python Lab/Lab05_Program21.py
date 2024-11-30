#                                                                       Program 21

#WAP to count the number of each character present in a string using the concept of a dictionary.

s=input("Enter the string:")
dict={}
t=s.split()
for i in t:
    for j in i:
        if(j not in dict):
            dict[j]=1
        else:
            dict[j]+=1
print(dict) 
