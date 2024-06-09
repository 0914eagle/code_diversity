
def get_group(num):
    if num in [1, 2, 3, 4, 5]:
        return 1
    elif num in [6, 7, 8, 9, 10]:
        return 2
    else:
        return 3

def check_same_group(x, y):
    return get_group(x) == get_group(y)

if __name__ == '__main__':
    x, y = map(int, input().split())
    print("Yes" if check_same_group(x, y) else "No")

