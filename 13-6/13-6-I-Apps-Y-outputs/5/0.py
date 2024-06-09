
def get_valid_expressions(a, b, c, d):
    expressions = []
    for operator1 in ["*", "+", "-", "/"]:
        for operator2 in ["*", "+", "-", "/"]:
            expression = str(a) + " " + operator1 + " " + str(b) + " " + operator2 + " " + str(c) + " " + operator2 + " " + str(d)
            try:
                result = eval(expression)
                expressions.append(expression)
            except ZeroDivisionError:
                pass
    return sorted(expressions)

def main():
    a, b, c, d = map(int, input().split())
    expressions = get_valid_expressions(a, b, c, d)
    if expressions:
        print("\n".join(expressions))
    else:
        print("problems ahead")

if __name__ == '__main__':
    main()

