
def get_valid_expressions(a, b, c, d):
    expressions = []
    for op1 in ['*', '+', '-', '/']:
        for op2 in ['*', '+', '-', '/']:
            for op3 in ['*', '+', '-', '/']:
                for op4 in ['*', '+', '-', '/']:
                    expression = f"{a} {op1} {b} {op2} {c} {op3} {d} {op4}"
                    try:
                        result = eval(expression)
                        if result:
                            expressions.append(expression)
                    except ZeroDivisionError:
                        pass
    return sorted(expressions)

def main():
    a, b, c, d = map(int, input().split())
    expressions = get_valid_expressions(a, b, c, d)
    if expressions:
        print(*expressions, sep='\n')
    else:
        print("problems ahead")

if __name__ == '__main__':
    main()

