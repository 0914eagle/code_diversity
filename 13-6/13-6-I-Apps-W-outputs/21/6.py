
import re

def parse_expression(expression):
    
    expression = expression.replace("(", " ( ").replace(")", " ) ")
    operators = []
    for match in re.finditer(r"\?", expression):
        operators.append((match.start(), match.end()))
    return expression, operators

def evaluate_expression(expression, operators):
    
    result = 0
    for operator in operators:
        value = 1 if expression[operator[0]:operator[1]] == "+" else -1
        result += value
    return result

def get_maximum_value(expression, plus_count, minus_count):
    
    # Parse the expression and get the list of operators
    expression, operators = parse_expression(expression)
    
    # Initialize the maximum value to 0
    maximum_value = 0
    
    # Iterate over all possible combinations of plus and minus operators
    for combination in itertools.product([1, -1], repeat=plus_count + minus_count):
        # Create a list of tuples containing the indices of the operators and their corresponding values
        operator_values = []
        for i in range(plus_count):
            operator_values.append((operators[i][0], combination[i]))
        for i in range(minus_count):
            operator_values.append((operators[-i - 1][0], combination[-i - 1]))
        
        # Sort the list of tuples by their indices in ascending order
        operator_values.sort(key=lambda x: x[0])
        
        # Replace the erased operators with the corresponding values and evaluate the expression
        for operator in operator_values:
            expression = expression[:operator[0]] + str(operator[1]) + expression[operator[0] + 1:]
        value = evaluate_expression(expression, operators)
        
        # Update the maximum value if the current value is greater than the previous maximum value
        if value > maximum_value:
            maximum_value = value
    
    return maximum_value

if __name__ == '__main__':
    expression = input()
    plus_count, minus_count = map(int, input().split())
    print(get_maximum_value(expression, plus_count, minus_count))

