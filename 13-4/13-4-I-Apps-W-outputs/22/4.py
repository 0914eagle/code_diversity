
def solve(expression):
    A, B, C = map(int, expression.split("+")[0].split("|")[1:])
    D, E = map(int, expression.split("=")[1].split("|")[1:])
    if A + B == C and A + D == E:
        return expression
    if A + B == C and A + D != E:
        return "|" + "|".join(str(i) for i in [A, B, D, E])
    if A + B != C and A + D == E:
        return "|" + "|".join(str(i) for i in [A, D, B, E])
    return "Impossible"

