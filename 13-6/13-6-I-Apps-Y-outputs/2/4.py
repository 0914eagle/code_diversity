
def get_group(n):
    if n % 4 == 1 or n % 4 == 2:
        return 1
    elif n % 4 == 3:
        return 2
    else:
        return 3

def is_same_group(x, y):
    return get_group(x) == get_group(y)

if __name__ == '__main__':
    x, y = map(int, input().split())
    print("Yes" if is_same_group(x, y) else "No")

