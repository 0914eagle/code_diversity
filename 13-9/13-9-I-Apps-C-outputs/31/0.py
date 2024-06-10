
def solve(expression, p, m):
    # Convert the expression to a polynomial
    poly = polynomial(expression)
    
    # Find the minimum non-negative value of x that satisfies the equation
    x = 0
    while poly.rem(m) != p:
        x += 1
        poly += 1
    
    return x

def polynomial(expression):
    # Convert the expression to a polynomial
    poly = 0
    for term in expression.split('+'):
        coeff, var = term.split('x')
        poly += int(coeff) * x**int(var)
    return poly

if __name__ == '__main__':
    expression, p, m = input().split()
    print(solve(expression, int(p), int(m)))

