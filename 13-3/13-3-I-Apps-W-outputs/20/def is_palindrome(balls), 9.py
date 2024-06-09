
def is_palindrome(balls):
    return balls == balls[::-1]

def can_make_palindrome(r, g, b, w):
    balls = [r, g, b, w]
    if is_palindrome(balls):
        return True
    if r == 0 and g == 0 and b == 0 and w == 0:
        return False
    if r >= 1 and g >= 1 and b >= 1:
        return False
    if r >= 1 and g >= 1 and w >= 1:
        return False
    if g >= 1 and b >= 1 and w >= 1:
        return False
    if r >= 1 and b >= 1 and w >= 1:
        return False
    if r >= 1 and g >= 1 and b >= 1 and w >= 1:
        return False
    return can_make_palindrome(r-1, g-1, b-1, w-1)

