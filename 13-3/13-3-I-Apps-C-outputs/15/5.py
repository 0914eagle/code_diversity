
def calculate_value(walk):
    value = 1
    for char in walk:
        if char == 'L':
            value = value * 2
        elif char == 'R':
            value = value * 2 + 1
        elif char == 'P':
            continue
        elif char == '*':
            value = value * 2 + 1
    return value

