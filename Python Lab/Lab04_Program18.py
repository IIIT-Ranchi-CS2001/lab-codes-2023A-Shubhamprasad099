#                                                                             Program 18

#Generate two sets – first for all singers and second for all dancers of the class using set comprehension.
#  Perform set operations to generate the following sets 
#a) of all artists of the class
#b) allrounders of the class
#c) dancers but not singers
#d) singers but not dancers
#e) dancers but not singers cum singers but not dancers

singers = {"Bheem", "Raju", "Jaggu", "Kalia"}
dancers = {"Chutki", "Indumati", "Bholu", "Dholu"}
all_artists = {i for i in singers.union(dancers)}
all_rounders = {i for i in singers.intersection(dancers)}
dancers_only = {i for i in dancers.difference(singers)}
singers_only = {i for i in singers.difference(dancers)}
diff = {i for i in dancers.symmetric_difference(singers)}

print("Singers:", singers)
print("Dancers:", dancers)
print("All Artists of class:", all_artists)
print("All-Rounders of the class:", all_rounders)
print("Dancers but not singers:", dancers_only)
print("Singers but not dancers:", singers_only)
print("Dancers but not Singers cum Singers but not Dancers:", diff)
