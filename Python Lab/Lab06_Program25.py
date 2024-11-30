#                                                                             Program 25

# Define a function my_sort() to sort the list of tuples created using my_zip function in the last question. 
# The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting:
# [Usage of built-in function sorted() is a punishable offense]
# Key = 0: sorting based on customer name in ascending order
# Key = 1: sorting based on Customer ID
# Key = 2: sorting based on shopping points

def my_sort(data, key=0):
    n = len(data)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    
    return data

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [102, 101, 103]
shopping_points = [500, 400, 600]

zipped_data = my_zip(customer_names, customer_ids, shopping_points, strct=True)

sorted_by_name = my_sort(zipped_data, key=0)
print("Sorted by customer name:", sorted_by_name)

sorted_by_id = my_sort(zipped_data, key=1)
print("Sorted by customer ID:", sorted_by_id)

sorted_by_points = my_sort(zipped_data, key=2)
print("Sorted by shopping points:", sorted_by_points)

