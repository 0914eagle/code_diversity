
def evaluate(formula):
    A, op, B = formula.split()
    if op == "+":
        return int(A) + int(B)
    else:
        return int(A) - int(B)

