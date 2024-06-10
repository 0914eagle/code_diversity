
def get_min_positive_divisible_not_in_segment(l, r, d):
    # Find the smallest positive integer that is divisible by d and does not belong to the segment [l, r]
    for x in range(l, r+1):
        if x % d == 0 and x not in range(l, r+1):
            return x
    return -1

def main():
    q = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        print(get_min_positive_divisible_not_in_segment(l, r, d))

if __name__ == '__main__':
    main()

