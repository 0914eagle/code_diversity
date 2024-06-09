
def is_multiple_of_4(r, g, b):
    num = int(str(r) + str(g) + str(b))
    if num % 4 == 0:
        return "YES"
    else:
        return "NO"

