
def solve(expression):
    A, B, C = map(int, expression.split('+')[0].split('|'))
    D, E = map(int, expression.split('=')[1].split('|'))
    if A + B == C and A + D == E:
        return expression
    if A + B == C and A + D != E:
        return f"{A}|+|{B}=|{D}|{E}"
    if A + B != C and A + D == E:
        return f"{A}|{B}|+|=|{D}|{E}"
    return "Impossible"
