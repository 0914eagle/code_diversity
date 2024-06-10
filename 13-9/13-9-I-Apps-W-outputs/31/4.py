
def get_minimum_positive_integer_divisible_by(d):
    for i in range(1, 10**9 + 1):
        if i % d == 0:
            return i
    return -1

def get_minimum_positive_integer_not_in_segment(l, r, d):
    if l % d == 0:
        return l + d
    else:
        return l + d - l % d

def main():
    q = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        print(get_minimum_positive_integer_not_in_segment(l, r, d))

if __name__ == '__main__':
    main()

