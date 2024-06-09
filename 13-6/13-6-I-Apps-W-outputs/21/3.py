
import re

def get_expression(expression):
    # Function to get the expression from the input string
    return re.findall(r'\d+|\?', expression)

def evaluate_expression(expression):
    # Function to evaluate the expression and return the result
    result = 0
    for token in expression:
        if token == '?':
            result += 1
        else:
            result = result * 10 + int(token)
    return result

def get_max_value(expression, plus_count, minus_count):
    # Function to get the maximum value of the expression by placing the plus and minus operators in the place of the erased operators
    expression = get_expression(expression)
    plus_count = int(plus_count)
    minus_count = int(minus_count)
    total_count = plus_count + minus_count
    if total_count == 0:
        return evaluate_expression(expression)
    max_value = 0
    for i in range(total_count + 1):
        # Generate all possible combinations of plus and minus operators
        plus_string = '+' * i
        minus_string = '-' * (total_count - i)
        current_expression = []
        for j, token in enumerate(expression):
            if token == '?':
                current_expression.append(plus_string if j % 2 == 0 else minus_string)
            else:
                current_expression.append(token)
        current_expression = ''.join(current_expression)
        current_value = evaluate_expression(current_expression)
        max_value = max(max_value, current_value)
    return max_value

if __name__ == '__main__':
    expression = input()
    plus_count, minus_count = input().split()
    print(get_max_value(expression, plus_count, minus_count))

