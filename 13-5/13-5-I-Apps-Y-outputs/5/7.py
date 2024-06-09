
def solve(expression):
    A, op, B = expression.split()
    if op == '+':
        return int(A) + int(B)
    else:
        return int(A) - int(B)

