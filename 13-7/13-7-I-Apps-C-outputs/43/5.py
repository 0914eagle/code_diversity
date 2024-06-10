
def get_minimal_x(expression, p, m):
    # Convert the expression to a list of tokens
    tokens = expression.split()
    
    # Initialize the minimum value of x as 0
    min_x = 0
    
    # Iterate through the tokens and check if the remainder of dividing the expression with m is equal to p
    for token in tokens:
        if token == 'x':
            min_x += 1
        elif token.isdigit():
            if (int(token) * min_x) % m != p:
                return -1
    
    # If the expression is valid, return the minimum value of x
    return min_x

def main():
    expression, p, m = input().split()
    p = int(p)
    m = int(m)
    print(get_minimal_x(expression, p, m))

if __name__ == '__main__':
    main()

