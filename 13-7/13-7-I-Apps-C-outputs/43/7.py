
import sys

def get_expression():
    return sys.stdin.readline().strip()

def get_parameters():
    return tuple(map(int, sys.stdin.readline().strip().split()))

def solve(expression, parameters):
    p, m = parameters
    x = 0
    while True:
        if (expression % m) == p:
            break
        x += 1
    return x

def main():
    expression = get_expression()
    parameters = get_parameters()
    print(solve(expression, parameters))

if __name__ == '__main__':
    main()

