
#                                                                             Program 26
# Write program to define a function my_max() to complete the following tasks: [Usage of built-in function max() is strictly prohibited]
# If a list of integers is passed as the input argument, the function shall return maximum value present in the list
# If a set is passed, maximum value present in the list
# If a tuple is passed, maximum value present in the tuple
# Hint: Pass the container type unpacked using *
def my_max(*numbers):   
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
numbers_list = [10, 20, 30, 40, 50]
print("Maximum value in list:", my_max(*numbers_list))
numbers_set = {100, 200, 300, 400, 500}
print("Maximum value in set:", my_max(*numbers_set))
numbers_tuple = (1000, 2000, 3000, 4000, 5000)
print("Maximum value in tuple:", my_max(*numbers_tuple))


