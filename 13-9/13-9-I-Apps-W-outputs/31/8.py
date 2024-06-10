
def get_min_positive_divisible(l, r, d):
    for i in range(l, r+1):
        if i % d == 0 and i not in range(l, r+1):
            return i
    return -1

def get_min_positive_divisible_efficient(l, r, d):
    if d > r:
        return -1
    return (d // l + 1) * l

def main():
    q = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        print(get_min_positive_divisible_efficient(l, r, d))

if __name__ == '__main__':
    main()

