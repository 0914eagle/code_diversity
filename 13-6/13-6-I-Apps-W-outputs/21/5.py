
def get_expression(expression):
    # Replace all '?' with '+'
    expression = expression.replace("?", "+")
    # Evaluate the expression
    return eval(expression)

def get_maximum_value(expression, num_plus, num_minus):
    # Get all possible combinations of '+' and '-' operators
    combinations = [(num_plus, num_minus)]
    if num_plus > 0:
        combinations += [(num_plus - 1, num_minus + 1)]
    if num_minus > 0:
        combinations += [(num_plus + 1, num_minus - 1)]
    
    # Get the maximum value for each combination
    maximum_value = 0
    for num_plus, num_minus in combinations:
        # Replace the first '?' with '+' and the second '?' with '-'
        expression = expression.replace("?", "+", 1).replace("?", "-", 1)
        value = get_expression(expression)
        if value > maximum_value:
            maximum_value = value
    
    return maximum_value

if __name__ == '__main__':
    expression = input()
    num_plus, num_minus = map(int, input().split())
    print(get_maximum_value(expression, num_plus, num_minus))

