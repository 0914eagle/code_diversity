
def power(x, y):
    return x ** y

def compare(x, y):
    x_power_y = power(x, y)
    y_power_x = power(y, x)
    if x_power_y < y_power_x:
        return '<'
    elif x_power_y > y_power_x:
        return '>'
    else:
        return '='

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(compare(x, y))

