
def is_palindrome(balls):
    return balls == balls[::-1]

def can_be_palindrome(r, g, b, w):
    balls = [r, g, b, w]
    if is_palindrome(balls):
        return True
    if r == 0 and g == 0 and b == 0 and w == 0:
        return False
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                if balls[i] > 0 and balls[j] > 0 and balls[k] > 0:
                    balls[i] -= 1
                    balls[j] -= 1
                    balls[k] -= 1
                    if can_be_palindrome(balls[0], balls[1], balls[2], balls[3]):
                        return True
                    balls[i] += 1
                    balls[j] += 1
                    balls[k] += 1
    return False

