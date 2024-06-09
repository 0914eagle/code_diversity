
def is_haiku(a, b, c):
    if a + b + c == 16 and a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
        return "YES"
    else:
        return "NO"

