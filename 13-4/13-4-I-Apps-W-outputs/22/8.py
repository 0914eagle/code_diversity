
def solve(expression):
    A, B, C = map(int, expression.split('+')[0].split('|'))
    C_ = int(expression.split('=')[1].split('|')[0])
    if A + B == C_:
        return expression
    if A + B != C_:
        return "Impossible"

