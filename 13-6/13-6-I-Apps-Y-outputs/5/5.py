
def get_expressions(a, b, c, d):
    expressions = []
    for op1 in ["+", "-", "*", "/"]:
        for op2 in ["+", "-", "*", "/"]:
            expr = f"{a} {op1} {b} {op2} {c} {op2} {d}"
            try:
                result = eval(expr)
                if result == 0:
                    expressions.append(expr)
            except ZeroDivisionError:
                pass
    return sorted(expressions)

def main():
    a, b, c, d = map(int, input().split())
    expressions = get_expressions(a, b, c, d)
    if expressions:
        for expr in expressions:
            print(expr)
    else:
        print("problems ahead")

if __name__ == '__main__':
    main()

