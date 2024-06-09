
def compare_numbers(x, y):
    x_str = "".join(str(i) for i in x)
    y_str = "".join(str(i) for i in y)
    if x_str == y_str:
        return "="
    elif x_str < y_str:
        return "<"
    else:
        return ">"

