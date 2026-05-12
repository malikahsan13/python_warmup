num1 = input("Enter num1 = ")
num2 = input("Enter num2 = ")
op = input("Enter operation +,-,/,* you want to perform")

if op == "+":
    print("Sum is = ", int(num1) + int(num2))
elif op == "-":
    print("Subtraction is = ",int(num1) - int(num2))
elif op == "/":
    if int(num2) !=0:
        print("Division num1/num2 = ", int(num1) / int(num2))
    else:
        print("Division not possible")
elif op == "*":
    print("Multiplication = ", int(num1) * int(num2))