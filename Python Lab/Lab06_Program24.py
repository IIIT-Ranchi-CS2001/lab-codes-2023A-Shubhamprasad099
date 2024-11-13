#                                                                            22-10-2024
#                                                                            LAB SESSION 6:
#                                                                                 Function
# 
#                                                                             Program 24

# Define a function my_zip() that can form a list of tuples by iterating the following customer 
# details:- ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: 
# If strct = True, zipping shall be done only if all lists are of equal length. If strct = False, 
# zipping can be done by taking the minimum length of the iterable.

def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All lists must be of equal length for strict zipping.")
    else:
        min_len = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_len)]

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [102, 101, 103]
shopping_points = [500, 400, 600]

try:
    zipped_data_strict = my_zip(customer_names, customer_ids, shopping_points, strct=True)
    print("Strict zipped data:", zipped_data_strict)
except ValueError as e:
    print(e)
    
zipped_data_non_strict = my_zip(customer_names, customer_ids, shopping_points, strct=False)
print("Non-strict zipped data:", zipped_data_non_strict)
