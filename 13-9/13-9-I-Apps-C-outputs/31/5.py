
def get_min_x(expression, p, m):
    # Replace all occurrences of x with 0
    expression = expression.replace("x", "0")
    
    # Evaluate the expression
    result = eval(expression)
    
    # Find the smallest non-negative value of x that satisfies the given condition
    for x in range(0, m):
        if (result + x) % m == p:
            return x
    
    # If no such value exists, return -1
    return -1

def main():
    expression, p, m = input().split()
    p = int(p)
    m = int(m)
    print(get_min_x(expression, p, m))

if __name__ == '__main__':
    main()

