
def get_group(n):
    if n <= 3:
        return 1
    elif n <= 6:
        return 2
    else:
        return 3

def solve(x, y):
    return "Yes" if get_group(x) == get_group(y) else "No"

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(solve(x, y))

