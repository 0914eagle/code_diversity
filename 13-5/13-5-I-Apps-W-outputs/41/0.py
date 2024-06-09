
def get_min_distance(x1, x2, x3):
    return abs(x1 - x2) + abs(x2 - x3) + abs(x3 - x1)

def get_input():
    x1, x2, x3 = map(int, input().split())
    return x1, x2, x3

if __name__ == '__main__':
    x1, x2, x3 = get_input()
    print(get_min_distance(x1, x2, x3))

