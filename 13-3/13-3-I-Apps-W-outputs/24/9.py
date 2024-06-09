
def compare_bases(x, y):
    x_base = int(x[0])
    x_digits = x[1:]
    y_base = int(y[0])
    y_digits = y[1:]
    
    x_num = 0
    for i in range(len(x_digits)):
        x_num += (x_base ** (len(x_digits) - i - 1)) * int(x_digits[i])
    
    y_num = 0
    for i in range(len(y_digits)):
        y_num += (y_base ** (len(y_digits) - i - 1)) * int(y_digits[i])
    
    if x_num < y_num:
        return '<'
    elif x_num > y_num:
        return '>'
    else:
        return '='

