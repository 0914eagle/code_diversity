
def is_valid_divisibility_hack(b, d):
    if not isinstance(b, int) or not isinstance(d, int):
        raise ValueError("b and d must be integers")
    if b < 2 or d < 2:
        return False
    if b == d:
        return True
    if d % 2 == 0:
        return False
    for i in range(3, int(d**0.5) + 1, 2):
        if d % i == 0:
            return False
    return True

def find_m(b, d):
    if not isinstance(b, int) or not isinstance(d, int):
        raise ValueError("b and d must be integers")
    if not is_valid_divisibility_hack(b, d):
        return None
    for m in range(1, b):
        if (b**m - 1) % d == 0:
            return m
    return None

if __name__ == '__main__':
    b, d = map(int, input().split())
    m = find_m(b, d)
    if m is None:
        print("no")
    else:
        print("yes")

