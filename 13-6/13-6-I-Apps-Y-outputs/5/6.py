
def get_operators(a, b, c, d):
    operators = ["+", "-", "*", "/"]
    valid_expressions = []
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                for op4 in operators:
                    expression = f"{a} {op1} {b} {op2} {c} {op3} {d} {op4}"
                    try:
                        result = eval(expression)
                        if result:
                            valid_expressions.append(expression)
                    except ZeroDivisionError:
                        pass
    return valid_expressions

def main():
    a, b, c, d = map(int, input().split())
    valid_expressions = get_operators(a, b, c, d)
    if valid_expressions:
        print("\n".join(sorted(valid_expressions)))
    else:
        print("problems ahead")

if __name__ == '__main__':
    main()

