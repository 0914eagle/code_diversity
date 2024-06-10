
def find_min_positive_integer(l, r, d):
    # Find the smallest number greater than or equal to l that is divisible by d
    x = (l // d + 1) * d
    # Check if x is within the range [l, r]
    if l <= x <= r:
        # If x is within the range, return the next number that is divisible by d and not in the range
        return x + d
    else:
        # If x is not within the range, return -1
        return -1

def main():
    q = int(input())
    for i in range(q):
        l, r, d = map(int, input().split())
        print(find_min_positive_integer(l, r, d))

if __name__ == '__main__':
    main()

