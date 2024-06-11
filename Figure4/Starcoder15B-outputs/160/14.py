def do_algebra(operator, operand):
    
    # your code here
    # raise NotImplementedError
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result


# + deletable=false editable=false nbgrader={"checksum": "36192430961372438204", "grade": true, "grade_id": "cell-1758941231815200", "locked": true, "points": 1, "schema_version": 1, "solution": false}
assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 1
assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) ==