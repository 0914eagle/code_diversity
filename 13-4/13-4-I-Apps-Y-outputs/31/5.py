
def solve(string):
    result = ""
    for i in range(len(string)):
        if string[i] != "<":
            result += string[i]
        elif i > 0 and string[i-1] != "<":
            result = result[:-1]
    return result

