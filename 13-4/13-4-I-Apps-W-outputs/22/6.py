
def solve(expression):
    A, B, C = map(int, expression.split('+')[-1].split('=')[:-1])
    if A + B == C:
        return expression
    else:
        for i in range(1, min(A, B) + 1):
            if A - i + B == C:
                return f'{A-i}|+|{B}=|{C}'
            elif A + B - i == C:
                return f'{A}|+|{B-i}=|{C}'
    return 'Impossible'

