number1 = int(input("Enter your first number: ")) 
number2 = int(input("Enter your second number: ")) 

print("Choose the operation: ")
print("+ : Addition")
print("- : subtraction")
print("* : multiplication")
print("/ : Division")
 
operation = input("choose an operation: ") 

if(operation == "+"):
    total = number1 + number2
    print(f"sum = {number1} + {number2} = {total}")
elif(operation == "-"):
    sub =number1 - number2
    print(f"Subtraction = {number1} - {number2} = {sub}")
elif(operation == "*"):
    product = number1 * number2
    print(f"product = {number1} * {number2} = {product}")    
elif(operation == "/"):
    division =number1 / number2
    print(f"Division {number1} / {number2} = {division}")    
else:
    print("Choose a valid symbol")  