#                                                                       Program 23

#Sort the list of tuples constructed above with and without sorted function. 
name = ['amit','rahul','aman']
id = [1001,1002,1003]
s_list = ['abc','xyz','jkl']
new = zip(name,id,s_list)
comb_zip = list(new)
comb_nozip = []
for i in range(len(name)):
    comb_nozip.append((name[i], id[i],s_list[i]))
print("Original:-",comb_nozip)
sorted_comb  = sorted(comb_zip)
print("With sorted function:-",sorted_comb)
n = len(comb_nozip)
for i in range(n):
    for j in range(0,n-i-1):
        if(comb_nozip[j]>comb_nozip[j+1]):
            comb_nozip[j],comb_nozip[j+1] = comb_nozip[j+1],comb_nozip[j]
print("Without sorted function:-",comb_nozip)
