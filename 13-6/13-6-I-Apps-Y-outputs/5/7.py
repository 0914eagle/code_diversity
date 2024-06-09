
def get_operators(a, b, c, d):
    operators = ["+", "-", "*", "/"]
    valid_expressions = []
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                expression = "{} {} {} {}".format(a, op1, b, op2)
                if eval(expression) == c:
                    expression = "{} {} {} {}".format(expression, op3, d)
                    if eval(expression) == True:
                        valid_expressions.append(expression)
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

