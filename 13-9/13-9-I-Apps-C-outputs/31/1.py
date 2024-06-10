
import math
import itertools

def parse_expression(expression):
    
    coefficients = []
    variable = None
    for token in expression.split():
        if token.isdigit():
            coefficients.append(int(token))
        elif token == 'x':
            variable = 'x'
        elif token in '+-':
            pass
        else:
            raise ValueError("Invalid token in expression: {}".format(token))
    return coefficients, variable

def find_solution(coefficients, variable, p, m):
    
    # Find the greatest common divisor of the coefficients and m
    gcd = math.gcd(m, *coefficients)
    # Divide the coefficients and m by the gcd
    coefficients = [coeff // gcd for coeff in coefficients]
    m //= gcd
    # Find the prime factors of m
    prime_factors = set(itertools.takewhile(lambda x: x <= int(math.sqrt(m)), itertools.count(2)))
    while len(prime_factors) > 0:
        # Try each prime factor as the solution
        for prime in prime_factors:
            # Check if the solution is valid
            if (prime * coefficients[0]) % m == p:
                return prime
        # Remove the smallest prime factor and try again
        prime_factors.remove(min(prime_factors))
    return None

def main():
    expression = input()
    p, m = map(int, input().split())
    coefficients, variable = parse_expression(expression)
    solution = find_solution(coefficients, variable, p, m)
    if solution is not None:
        print(solution)
    else:
        print("No solution found")

if __name__ == '__main__':
    main()

