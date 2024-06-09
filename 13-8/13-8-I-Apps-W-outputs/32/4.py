
def get_string(n):
    if n == 1:
        return "a"
    if n == 2:
        return "aa"
    if n == 3:
        return "bba"
    # general case
    string = "c" * (n - 1)
    for i in range(n - 2, -1, -1):
        if string[i] == "c":
            string = string[:i] + "b" + string[i:]
        else:
            string = string[:i] + "a" + string[i:]
    return string

