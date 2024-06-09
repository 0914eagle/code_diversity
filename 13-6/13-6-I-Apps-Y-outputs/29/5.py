
def solve(input_string):
    result = ""
    for char in input_string:
        if char == "<":
            result = result[:-1]
        else:
            result += char
    return result

