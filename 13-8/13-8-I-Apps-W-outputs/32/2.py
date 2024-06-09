
def get_string(n):
    if n == 1:
        return "a"
    if n == 2:
        return "aa"
    if n == 3:
        return "bba"
    string = "a" * (n-1)
    for i in range(1, n):
        if i % 2 == 0:
            string = string[:i] + "b" + string[i:]
        else:
            string = string[:i] + "c" + string[i:]
    return string

