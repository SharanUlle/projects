a = int(input("Enter the first term:"))
d = int(input("Enter the common difference:"))
n = int(input("Enter the number of terms:"))
for t in range(a,a+d*n,d):
    print(t)