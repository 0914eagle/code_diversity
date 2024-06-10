
def can_multiply(a, b):
    if a == 1:
        return True
    if a == 2 and b <= 9:
        return True
    if a == 3 and b <= 3:
        return True
    if a == 4 and b <= 2:
        return True
    if a == 5 and b == 1:
        return True
    if a == 6 and b <= 2:
        return True
    if a == 7 and b == 1:
        return True
    if a == 8 and b <= 3:
        return True
    if a == 9 and b == 1:
        return True
    return False

def multiply(a, b):
    if can_multiply(a, b):
        return a * b
    else:
        return -1

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(multiply(a, b))

