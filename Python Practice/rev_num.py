n = int(input("enter the number:"))
rev = 0
while n >0:
    rem = n % 10
    rev = rev * 10 + rem
    n = int(n/10)
print("reverse of a number is " , rev)