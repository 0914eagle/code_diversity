
def get_expression(expression):
    return expression.split('+')

def get_min_value(expression, p, m):
    x = 0
    while True:
        if (int(expression.replace('x', str(x))) % m) == p:
            return x
        x += 1

def main():
    expression = input()
    p, m = map(int, input().split())
    print(get_min_value(expression, p, m))

if __name__ == '__main__':
    main()

