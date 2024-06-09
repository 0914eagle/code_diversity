
def solve(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "<":
            if i > 0 and string[i-1] != "<":
                result = result[:-1]
        else:
            result += string[i]
    return result

