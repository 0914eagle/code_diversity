
def compare_numbers(x_digits, x_base, y_digits, y_base):
    x_num = int(x_digits, x_base)
    y_num = int(y_digits, y_base)
    if x_num < y_num:
        return '<'
    elif x_num > y_num:
        return '>'
    else:
        return '='

