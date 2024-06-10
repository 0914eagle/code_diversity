
import re

def evaluate(expression, x):
    return eval(expression.replace("x", str(x)))

def find_minimal_x(expression, p, m):
    for x in range(m):
        if evaluate(expression, x) % m == p:
            return x
    return -1

def main():
    expression = input()
    p, m = map(int, input().split())
    print(find_minimal_x(expression, p, m))

if __name__ == '__main__':
    main()

