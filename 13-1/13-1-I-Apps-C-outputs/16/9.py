
def solve(string, explosion):
    while explosion in string:
        index = string.index(explosion)
        string = string[:index] + string[index+len(explosion):]
    if string == "":
        return "FRULA"
    else:
        return string

