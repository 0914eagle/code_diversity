
def compare_xy_with_yx(x, y):
    x_power_y = x**y
    y_power_x = y**x
    if x_power_y < y_power_x:
        return '<'
    elif x_power_y > y_power_x:
        return '>'
    else:
        return '='

def main():
    x, y = map(int, input().split())
    print(compare_xy_with_yx(x, y))

if __name__ == '__main__':
    main()

