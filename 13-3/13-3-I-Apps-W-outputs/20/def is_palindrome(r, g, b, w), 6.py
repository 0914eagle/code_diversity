
def is_palindrome(r, g, b, w):
    total_balls = r + g + b + w
    if total_balls % 2 == 1:
        return "No"
    else:
        half = total_balls // 2
        if r >= half and g >= half and b >= half and w >= half:
            return "Yes"
        else:
            return "No"

