
def get_group(num):
    if num <= 3:
        return 1
    elif num <= 6:
        return 2
    else:
        return 3

def same_group(x, y):
    return get_group(x) == get_group(y)

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(same_group(x, y))

