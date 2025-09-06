# Python program to display the multiplication table

def display_multiplication_table(number, max_multiplier):
    # Loop from 1 to the specified range
    for i in range(1, max_multiplier + 1):
        # Calculate the product
        product = number * i
        # Display the result
        print(f"{number} x {i} = {product}")

# Take input from the user for the number and range
number = int(input("Enter the number for which you want the multiplication table: "))
max_multiplier = int(input("Enter the maximum multiplier: "))

# Display the multiplication table for the chosen number and range
display_multiplication_table(number, max_multiplier)



num =int(input("Enter the number:"))
for i in range(1,11):
#  print(num, 'x', i, '=', num*i)
 print(f"{num} * {i} = {num * i}")