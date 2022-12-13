def resulting_expression(expression):
    if sum([1 for i in expression if i in ['+', '-', '*', '/']]) != 1:
        return "Invalid expression"
    if "+" in expression:
        values = tuple(map(float, expression.split("+")))
        return float(values[0]) + float(values[1])
    elif "-" in expression:
        values = tuple(map(float, expression.split("-")))
        return float(values[0]) - float(values[1])
    elif "*" in expression:
        values = tuple(map(float, expression.split("*")))
        return float(values[0]) * float(values[1])
    elif "/" in expression:
        values = tuple(map(float, expression.split("/")))
        if values[1] == 0:
            return "Division by zero!"
        return float(values[0]) / float(values[1])
    else:
        return print("Invalid expression")

def main():
    while True:
        expression = input()
        result = resulting_expression(expression)
        print(result)

if __name__ == '__main__':
    main()