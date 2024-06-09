
def is_palindrome(balls):
    return balls == balls[::-1]

def can_make_palindrome(r, g, b, w):
    balls = [r, g, b, w]
    if is_palindrome(balls):
        return True
    if r > 0 and g > 0 and b > 0:
        r -= 1
        g -= 1
        b -= 1
        w += 3
        return can_make_palindrome(r, g, b, w)
    return False

