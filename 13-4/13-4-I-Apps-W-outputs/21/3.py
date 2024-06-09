
def make_a_and_b_equal(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    if a == 0 and b == 0:
        return "YES"
    else:
        return "NO"

