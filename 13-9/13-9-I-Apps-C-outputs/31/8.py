
def parse_expression(expression):
    # Function to parse the expression and return a list of tuples containing the operation and the operands
    operation_map = {
        "+": "+",
        "-": "-",
        "*": "*",
    }
    operands = []
    current_operand = ""
    for char in expression:
        if char in operation_map:
            if current_operand != "":
                operands.append((current_operand, operation_map[char]))
                current_operand = ""
            else:
                operands.append(("0", operation_map[char]))
        elif char.isdigit():
            current_operand += char
        elif char == "x":
            current_operand += char
        else:
            raise ValueError("Invalid character in expression")
    if current_operand != "":
        operands.append((current_operand, "+"))
    return operands

def evaluate_expression(expression, x):
    # Function to evaluate the expression for a given value of x
    operands = parse_expression(expression)
    result = 0
    for operand, operation in operands:
        if operation == "+":
            result += int(operand)
        elif operation == "-":
            result -= int(operand)
        elif operation == "*":
            result *= int(operand)
        else:
            raise ValueError("Invalid operation in expression")
    return result

def find_min_x(expression, p, m):
    # Function to find the minimum value of x such that the remainder of dividing the expression with m is equal to p
    l, r = 0, m
    while l <= r:
        mid = (l + r) // 2
        if evaluate_expression(expression, mid) % m == p:
            if mid == 0 or evaluate_expression(expression, mid - 1) % m != p:
                return mid
            else:
                r = mid - 1
        else:
            l = mid + 1
    return -1

if __name__ == '__main__':
    expression = input()
    p, m = map(int, input().split())
    print(find_min_x(expression, p, m))

