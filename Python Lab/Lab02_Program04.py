#                                                                       Lab-2 STRING MANIPULATION
#
#                                                                         03-09-2024
#                                                                        Program 4
# If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
# a. “mAHA bHARAT”
# b. “Bharat”
# c. “BharatBharatBharat”
# d. “Mera Bharat”
# e. “Mera Bharat Mahan”
S1= "Maha Bharat"
print(S1.swapcase())
print(S1.split()[1])
print((S1.split()[1])*3)
print(S1.replace("Maha","Mera"))
print(S1.replace("Maha","Mera")+ " "+ "Mahan")
