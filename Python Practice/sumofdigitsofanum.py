n = int(input("Enter the number:"))
sum = 0
while n > 0:
    rem = (n % 10)
    sum = sum + rem
    n = int(n/10)
print ("sum of digits a number is",sum)