def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y==0:
      return "Error! Division by 0 is not defined"
    return x / y
def calculator():
    print("select operation:")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    while True:
     choice  = input("Enter the choice (1/2/3/4):")


     if choice in ['1', '2', '3', '4']:
          try:
              num1 = int(input("Enter the first number :"))
              num2 = int(input("Enter the second number :"))
          except ValueError:
               print("Value Error! . Please enter numeric values")
               continue
          if choice == '1':
               print(f"{num1} + {num2} = {add(num1,num2)}")
          elif choice == '2':
               print(f"{num1} - {num2} = {sub(num1,num2)}")
          elif choice == '3':
             print(f"{num1} * {num2} = {mul(num1,num2)}")
          elif choice == '4':
             print(f"{num1} / {num2} = {div(num1,num2)}")
     else:
             print("Invalid Choice! Please chose again")
     next_calculation = input("Do you want to perform another calculation? (yes/no): ")
     if next_calculation.lower() != 'yes':
            break
if __name__ == "__main__":
    calculator()