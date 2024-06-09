
def hex_compare(x, y):
    x_val = hex_to_dec(x)
    y_val = hex_to_dec(y)
    if x_val < y_val:
        return "<"
    elif x_val > y_val:
        return ">"
    else:
        return "="

def hex_to_dec(hex_str):
    hex_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    return hex_dict[hex_str]

x, y = input().split()
print(hex_compare(x, y))

