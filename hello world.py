print("Simple Arithemetic Calculator Designed By Dark~Knight")

firstvalue = int(input("Input a value:  "))
operator = input("Input an operator:    ")
secondvalue = int(input("Input a value: "))

if operator == "+":
    print(firstvalue + secondvalue)
elif operator == "-":
    print(firstvalue - secondvalue)
elif operator == "*":
    print(firstvalue * secondvalue)
elif operator == "/":
    print(firstvalue / secondvalue)
elif operator == str:
    print("Input an operator")
else:
    print("Not an operator")