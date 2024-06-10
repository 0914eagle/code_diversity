
def get_min_diff(weights):
    # find the minimum absolute difference of S_1 and S_2 for all possible T
    min_diff = float('inf')
    for T in range(1, len(weights)):
        S1 = sum(weights[:T])
        S2 = sum(weights[T:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    return min_diff

def main():
    # read input from stdin
    N = int(input())
    weights = list(map(int, input().split()))

    # call get_min_diff function and print result
    print(get_min_diff(weights))

if __name__ == '__main__':
    main()

