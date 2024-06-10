
def parse_expression(expression):
    # Function to parse the expression and return a tuple of the coefficients and variables
    coeffs, vars = [], []
    for token in expression.split():
        if token.isdigit():
            coeffs.append(int(token))
        elif token.lower() == "x":
            vars.append(token)
        else:
            coeffs.append(token)
    return coeffs, vars

def get_min_x(expression, p, m):
    # Function to find the minimum value of x that satisfies the given condition
    coeffs, vars = parse_expression(expression)
    x = 0
    while True:
        rem = 0
        for i in range(len(coeffs)):
            if vars[i] == "x":
                rem += coeffs[i] * x
            else:
                rem += coeffs[i]
        if rem % m == p:
            break
        x += 1
    return x

def main():
    expression, p, m = input().split()
    print(get_min_x(expression, int(p), int(m)))

if __name__ == '__main__':
    main()

