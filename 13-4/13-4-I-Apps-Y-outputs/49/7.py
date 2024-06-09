
def hex_compare(x, y):
    x_value = hex_to_decimal(x)
    y_value = hex_to_decimal(y)
    if x_value < y_value:
        return "<"
    elif x_value > y_value:
        return ">"
    else:
        return "="

def hex_to_decimal(hex_string):
    hex_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    return hex_dict[hex_string]

x, y = input().split()
print(hex_compare(x, y))

