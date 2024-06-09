
def is_poor_triplet(a, b, c):
    if a == b and b != c:
        return "Yes"
    elif a == c and b != a:
        return "Yes"
    elif b == c and a != b:
        return "Yes"
    else:
        return "No"

