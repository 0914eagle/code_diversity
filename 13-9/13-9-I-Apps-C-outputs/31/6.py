
import re

def get_min_x(expression, p, m):
    # Find all occurrences of x in the expression
    x_occurrences = re.findall(r"x", expression)
    
    # If there are no occurrences of x, return 0
    if not x_occurrences:
        return 0
    
    # If there is only one occurrence of x, return 1
    if len(x_occurrences) == 1:
        return 1
    
    # If there are multiple occurrences of x, find the minimum non-negative value of x that satisfies the remainder condition
    min_x = 1
    while True:
        # Calculate the value of the expression with the current value of x
        value = eval(expression.replace("x", str(min_x)))
        
        # If the value is divisible by m and the remainder is equal to p, return the current value of x
        if value % m == p:
            return min_x
        
        # Increment x and try again
        min_x += 1

def main():
    expression, p, m = input().split()
    p, m = int(p), int(m)
    print(get_min_x(expression, p, m))

if __name__ == '__main__':
    main()

