def do_algebra(operator, operand):
    
    # Your code here
    # 1. Check if the length of operator list is equal to the length of operand list minus one.
    if len(operator) != len(operand) - 1:
        return None
    # 2. Operand is a list of of non-negative integers.
    for i in operand:
        if i < 0:
            return None
    # 3. Operator list has at least one operator, and operand list has at least two operands.
    if len(operator) < 1 or len(operand) < 2:
        return None
    # 4. Use the two given lists to build the algebric expression and return the evaluation of this expression.
    # 4.1. Use the first operator in the operator list to combine the first two operands in the operand list.
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result **= operand[i + 1]
    return result


print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [2,