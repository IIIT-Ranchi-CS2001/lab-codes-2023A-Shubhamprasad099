#                                                                            24-09-2024
#                                                                            LAB SESSION 4:
#                                                                   CONTAINER TYPES IN PYTHON – LIST , SET
# 
#                                                                             Program 15

#Find the number of palindrome words in the given sentence without defining any new function (feel free to use python’s in-built functions).


a = input("Enter a sentence: ")
words = a.split()
count = 0 
for word in words:
       if(word.lower() == word[::-1].lower()):
        count += 1
print("Number of palindrome words:", count)

