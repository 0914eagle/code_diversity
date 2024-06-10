
def get_minimum_positive_integer_divisible_by_d_and_not_in_segment(l, r, d):
    # Find the smallest positive integer that is divisible by d and not in the segment [l, r]
    for x in range(d, r+1, d):
        if x < l:
            return x
    return -1

def get_minimum_positive_integer_divisible_by_d_and_not_in_segment_v2(l, r, d):
    # Find the smallest positive integer that is divisible by d and not in the segment [l, r]
    # This version uses a set to keep track of the numbers in the segment
    numbers = set(range(l, r+1))
    for x in range(d, r+1, d):
        if x not in numbers:
            return x
    return -1

def main():
    q = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        print(get_minimum_positive_integer_divisible_by_d_and_not_in_segment_v2(l, r, d))

if __name__ == '__main__':
    main()

