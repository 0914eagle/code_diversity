def do_algebra(operator, operand):
    
    # Initialize the result to 0
    result = 0

    # Iterate through the operator list
    for i in range(len(operator)):
        # If the operator is addition, multiply the operand and add the result
        if operator[i] == '+':
            result += operand[i]
        # If the operator is subtraction, subtract the operand and add the result
        elif operator[i] == '-':
            result += operand[i]
        # If the operator is multiplication, multiply the operand and add the result
        elif operator[i] == '*':
            result += operand[i]
        # If the operator is floor division, divide the operand by the result and add the result
        elif operator[i] == '//':
            result += operand[i]
        # If the operator is exponentiation, multiply the operand and add the result
        elif operator[i] == '**':
            result += operand[i]

    return result


