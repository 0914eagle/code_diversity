
import re

def get_expression(expression):
    
    return re.search(r'\d+[+\-*/()x ]+\d+', expression).group()

def get_p_and_m(expression):
    
    p = int(re.search(r'(\d+) (\d+)', expression).group(1))
    m = int(re.search(r'(\d+) (\d+)', expression).group(2))
    return p, m

def get_x(expression, p, m):
    
    x = 0
    while (expression % m) != p:
        x += 1
        expression = expression + 1
    return x

def solve(expression, p, m):
    
    expression = get_expression(expression)
    p, m = get_p_and_m(expression)
    x = get_x(expression, p, m)
    return x

if __name__ == '__main__':
    expression = input()
    p, m = map(int, input().split())
    result = solve(expression, p, m)
    print(result)

