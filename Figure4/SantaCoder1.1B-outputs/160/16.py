def do_algebra(operator, operand):
    
    # Initialize the result to 0
    result = 0
    # Initialize the operand list
    operand_list = operand[:]
    # Initialize the operator list
    operator_list = operator[:]
    # Iterate through the operator list
    for i in range(len(operator_list)):
        # Get the operator
        operator = operator_list[i]
        # Get the operand
        operand = operand_list[i]
        # If the operator is addition, subtract, multiply, or divide
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result //= operand
        elif operator == '**':
            result **= operand
    return result

# Test cases
print(do_algebra([1, 2, 3], [1, 2, 3]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5, 6]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5, 6, 7]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(do_algebra([1, 2, 3], [1, 2, 3, 4, 5