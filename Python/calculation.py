def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick operation: ")


calculation_function = operation[operation_symbol]
answer = calculation_function(num1,num2)

print(answer)