
def solve(expression):
    A, B, C = map(int, expression.split("+")[0].split("=")[0])
    D = int(expression.split("+")[0].split("=")[1])
    E = int(expression.split("+")[1][:-1])
    if A + B == C and D + E == C:
        return expression
    if A + B == C and D + E != C:
        return f"{A}+{B}={C}"
    if A + B != C and D + E == C:
        return f"{D}+{E}={C}"
    if A + B != C and D + E != C:
        return "Impossible"

