
def solve(expression, p, m):
    # convert the expression to a polynomial
    polynomial = poly(expression)
    
    # find the roots of the polynomial
    roots = polynomial.all_roots()
    
    # find the root with the smallest non-negative value that gives a remainder of p when divided by m
    for root in roots:
        if root >= 0 and polynomial(root) % m == p:
            return root
    
    # if no root is found, return -1
    return -1

def poly(expression):
    # convert the expression to a polynomial
    poly = sympy.Poly(expression, x)
    return poly

if __name__ == '__main__':
    expression, p, m = input().split()
    print(solve(expression, int(p), int(m)))

