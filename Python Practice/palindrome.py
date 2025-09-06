num = input("Enter a number: ")

# Check if the number is the same when reversed
if num == num[ ::-1]:
    print(num,"num is a palindrome.")
else:
    print(num,"num is not a palindrome.")
