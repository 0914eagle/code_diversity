
def parse_expression(expression):
    # Function to parse the expression and return a list of tuples containing the operation and the operands
    operations = ["+", "-", "*"]
    operands = []
    for char in expression:
        if char in operations:
            operands.append(char)
        elif char.isdigit():
            operands.append(int(char))
    return list(zip(operands[0::2], operands[1::2]))

def evaluate_expression(expression, x):
    # Function to evaluate the expression for a given value of x
    if expression[1] == "x":
        return x
    else:
        return expression[1]

def find_min_x(expression, p, m):
    # Function to find the minimal non-negative value of x for which the remainder of dividing the expression with m is equal to p
    min_x = 0
    while True:
        result = evaluate_expression(expression, min_x) % m
        if result == p:
            break
        min_x += 1
    return min_x

def main():
    expression = input()
    p, m = map(int, input().split())
    parsed_expression = parse_expression(expression)
    print(find_min_x(parsed_expression, p, m))

if __name__ == '__main__':
    main()

