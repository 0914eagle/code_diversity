
def solve(input_string):
    result = ""
    for i in range(len(input_string)):
        if input_string[i] == "<":
            if i > 0 and input_string[i-1] != "<":
                result = result[:-1]
        else:
            result += input_string[i]
    return result

