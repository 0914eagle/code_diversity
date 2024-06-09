
def compare_bases(x_digits, x_base, y_digits, y_base):
    x_num = 0
    y_num = 0
    for i in range(len(x_digits)):
        x_num += x_digits[i] * x_base ** (len(x_digits) - i - 1)
        y_num += y_digits[i] * y_base ** (len(y_digits) - i - 1)
    if x_num < y_num:
        return '<'
    elif x_num > y_num:
        return '>'
    else:
        return '='

