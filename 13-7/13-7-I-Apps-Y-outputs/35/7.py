
def solve(s):
    string = ""
    for key in s:
        if key == "0":
            string += "0"
        elif key == "1":
            string += "1"
        elif key == "B" and string:
            string = string[:-1]
    return string

