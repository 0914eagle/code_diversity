
def evaluate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += i**b
    return result % a

