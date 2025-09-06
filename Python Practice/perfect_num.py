# num = int(input("Enetr the number:"))
# per_num = 2

# #if per_num == num:
# print(num,"is perfect number")



def is_perfect_number(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    # Calculate the sum of proper divisors
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Input a number to check
number = int(input("Enter a number to check if it's perfect: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number!")
else:
    print(f"{number} is not a perfect number.")




#ANSWER
