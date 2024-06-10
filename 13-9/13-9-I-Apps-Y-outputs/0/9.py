
def get_min_diff(weights, T):
    # Calculate the sum of the weights in the first group
    sum_1 = sum(weights[:T])
    # Calculate the sum of the weights in the second group
    sum_2 = sum(weights[T:])
    # Return the absolute difference between the two sums
    return abs(sum_1 - sum_2)

def solve(weights):
    # Find the minimum absolute difference for all possible values of T
    min_diff = float('inf')
    for T in range(1, len(weights)):
        diff = get_min_diff(weights, T)
        if diff < min_diff:
            min_diff = diff
    # Return the minimum absolute difference
    return min_diff

if __name__ == '__main__':
    # Read the input data
    N = int(input())
    weights = [int(x) for x in input().split()]
    # Solve the problem
    result = solve(weights)
    # Print the result
    print(result)

