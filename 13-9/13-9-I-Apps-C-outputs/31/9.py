
import math
import re

def get_expression(expression):
    
    return re.findall(r"\d+|\+|\-|\*|\(|\)|\*|\*x|\(x", expression)

def get_variables(expression):
    
    variables = []
    for token in expression:
        if token == "x":
            variables.append(token)
    return variables

def get_coefficients(expression):
    
    coefficients = []
    for token in expression:
        if token.isdigit():
            coefficients.append(int(token))
    return coefficients

def get_remainder(expression, modulus, variable):
    
    coeffs = get_coefficients(expression)
    variables = get_variables(expression)
    expr = 0
    for i, coeff in enumerate(coeffs):
        if variables[i] == variable:
            expr += coeff
    return expr % modulus

def solve(expression, modulus, variable):
    
    min_x = 0
    for x in range(modulus):
        remainder = get_remainder(expression, modulus, variable)
        if remainder == modulus - 1:
            return min_x
        min_x += 1
    return -1

def main():
    expression = input()
    modulus, variable = map(int, input().split())
    print(solve(expression, modulus, variable))

if __name__ == '__main__':
    main()

