
def solve(expression):
    A, B, C = map(int, expression.split("+")[0].split("|"))
    C_ = int(expression.split("=")[1].strip("|"))
    if A + B == C_:
        return expression
    
    for i in range(A, C_):
        if (A + i) == C_:
            return f"||{A}+{i}={C_}"
    
    return "Impossible"

