
def get_string(n):
    if n == 1:
        return "a"
    if n == 2:
        return "aa"
    if n % 2 == 0:
        return "a" + get_string(n-1)
    else:
        return "b" + get_string(n-1)

