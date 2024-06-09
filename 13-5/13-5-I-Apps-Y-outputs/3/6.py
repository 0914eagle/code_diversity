
def solve(ticket):
    A, B, C, D = map(int, ticket)
    for op1 in "+-":
        for op2 in "+-":
            for op3 in "+-":
                if eval(f"A {op1} B {op2} C {op3} D") == 7:
                    return f"{A}{op1}{B}{op2}{C}{op3}{D}=7"

