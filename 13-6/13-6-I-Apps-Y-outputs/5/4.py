
def get_valid_expressions(a, b, c, d):
    valid_expressions = []
    for operator1 in ['+', '-', '*', '/']:
        for operator2 in ['+', '-', '*', '/']:
            expression = f"{a} {operator1} {b} = {c} {operator2} {d}"
            try:
                result = eval(expression)
                if result:
                    valid_expressions.append(expression)
            except ZeroDivisionError:
                pass
    return valid_expressions

def main():
    a, b, c, d = map(int, input().split())
    valid_expressions = get_valid_expressions(a, b, c, d)
    if valid_expressions:
        print(*valid_expressions, sep='\n')
    else:
        print("problems ahead")

if __name__ == '__main__':
    main()

