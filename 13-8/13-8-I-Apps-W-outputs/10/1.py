
def compare(x, y):
    x_pow_y = x**y
    y_pow_x = y**x
    if x_pow_y < y_pow_x:
        return '<'
    elif x_pow_y > y_pow_x:
        return '>'
    else:
        return '='

def main():
    x, y = map(int, input().split())
    print(compare(x, y))

if __name__ == '__main__':
    main()

