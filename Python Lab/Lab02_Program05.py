#                                                          Program 5
# For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
#1 The length of the string S
#2 The first occurrence of the letter ‘e’
#3 The total number of occurrences of ‘a’
#4 Generate “Ta Ta Black Sheep”
S='Ba Ba Black Sheep'
print(len(S))
print(S.find('e'))
print(S.count('a'))
print(S.replace("Ba","Ta"))
