
def get_min_abs_diff(weights):
    # Find the minimum absolute difference between the sums of the weights
    # in the two groups by iterating through all possible values of T
    min_abs_diff = float('inf')
    for T in range(1, len(weights)):
        sum1 = sum(weights[:T])
        sum2 = sum(weights[T:])
        abs_diff = abs(sum1 - sum2)
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff

def main():
    # Read the input data from stdin
    num_weights = int(input())
    weights = list(map(int, input().split()))

    # Call the get_min_abs_diff function and print the result
    print(get_min_abs_diff(weights))

if __name__ == '__main__':
    main()

