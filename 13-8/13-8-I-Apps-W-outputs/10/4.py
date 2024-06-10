
def x_pow_y(x, y):
    return x ** y

def y_pow_x(x, y):
    return y ** x

def compare(x, y):
    if x_pow_y(x, y) < y_pow_x(x, y):
        return '<'
    elif x_pow_y(x, y) > y_pow_x(x, y):
        return '>'
    else:
        return '='

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(compare(x, y))

