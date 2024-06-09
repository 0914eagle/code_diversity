
def evaluate_expression(expression, num_plus, num_minus):
    # Replace the ? with + or - based on the number of plus and minus operators
    for i in range(num_plus):
        expression = expression.replace("?", "+", 1)
    for i in range(num_minus):
        expression = expression.replace("?", "-", 1)

    # Evaluate the expression
    return eval(expression)

def main():
    expression = input()
    num_plus, num_minus = map(int, input().split())
    print(evaluate_expression(expression, num_plus, num_minus))

if __name__ == '__main__':
    main()

