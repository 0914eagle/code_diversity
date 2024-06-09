
def is_palindrome(balls):
    return balls == balls[::-1]

def solve(balls):
    r, g, b, w = balls
    if r + g + b + w == 0:
        return "Yes"
    if r % 2 == 1 or g % 2 == 1 or b % 2 == 1:
        return "No"
    r //= 2
    g //= 2
    b //= 2
    w //= 2
    return "Yes" if is_palindrome((r, g, b, w)) else "No"

