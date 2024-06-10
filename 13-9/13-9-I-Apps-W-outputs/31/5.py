
def find_min_divisible(l, r, d):
    # Find the smallest number greater than or equal to l that is divisible by d
    x = (l // d + 1) * d
    while x <= r:
        if x % d == 0:
            return x
        x += d
    return -1

def find_min_not_divisible(l, r, d):
    # Find the smallest number greater than or equal to l that is not divisible by d
    x = l
    while x <= r:
        if x % d != 0:
            return x
        x += 1
    return -1

def find_min_not_in_segment(l, r, d):
    # Find the smallest number greater than or equal to l that is not in the segment [l, r]
    x = l
    while x <= r:
        if x not in range(l, r + 1):
            return x
        x += 1
    return -1

def main():
    q = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        print(find_min_not_in_segment(l, r, d))

if __name__ == '__main__':
    main()

