 #                                                                      Program 22


#Enter three lists using list comprehension: Customer name, Customer ID, and shopping points.
#  Construct a list of tuples with and without using built-in function zip().

num_customers = int(input("Enter number of customers: "))
customer_name = [input(f"Enter Customer {i+1} name: ") for i in range(num_customers)]
customer_id = [input(f"Enter Customer {i+1} ID: ") for i in range(num_customers)]
shopping_points = [int(input(f"Enter Customer {i+1} shopping points: ")) for i in range(num_customers)]
customer_data_without_zip = [(name, id, points) for name, id, points in zip(customer_name, customer_id, shopping_points)]
customer_data_with_zip = list(zip(customer_name, customer_id, shopping_points))

print("\nCustomer Data without zip():", customer_data_without_zip)
print("\nCustomer Data with zip():", customer_data_with_zip)

