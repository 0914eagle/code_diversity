
def get_valid_expressions(a, b, c, d):
    expressions = []
    for op1 in ['+', '-', '*', '/']:
        for op2 in ['+', '-', '*', '/']:
            try:
                result = eval(f'{a} {op1} {b} {op2} {c} {op2} {d}')
                expressions.append(f'{a} {op1} {b} = {c} {op2} {d}')
            except ZeroDivisionError:
                pass
    return sorted(expressions)

def main():
    a, b, c, d = map(int, input().split())
    expressions = get_valid_expressions(a, b, c, d)
    if expressions:
        print('\n'.join(expressions))
    else:
        print('problems ahead')

if __name__ == '__main__':
    main()

