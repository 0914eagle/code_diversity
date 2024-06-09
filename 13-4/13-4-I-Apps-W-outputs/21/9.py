
def make_a_and_b_equal_to_zero(a, b):
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a == 0 and b == 0

