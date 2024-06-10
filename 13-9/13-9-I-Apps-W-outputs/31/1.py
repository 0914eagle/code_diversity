
def get_min_divisible(l, r, d):
    for i in range(l, r+1):
        if i % d == 0 and i not in range(l, r+1):
            return i
    return -1

def get_min_divisible_alt(l, r, d):
    for i in range(l, r+1):
        if i % d == 0 and i not in range(l, r+1):
            return i
    return -1

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        print(get_min_divisible(l, r, d))

