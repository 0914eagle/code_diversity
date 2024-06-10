
def get_expected_sum(dice_values):
    # Calculate the expected sum of the dice
    expected_sum = 0
    for value in dice_values:
        expected_sum += value
    return expected_sum

def get_maximum_expected_sum(dice_values, k):
    # Calculate the maximum expected sum of k adjacent dice
    maximum_expected_sum = 0
    for i in range(len(dice_values) - k + 1):
        expected_sum = get_expected_sum(dice_values[i:i+k])
        if expected_sum > maximum_expected_sum:
            maximum_expected_sum = expected_sum
    return maximum_expected_sum

def main():
    # Read the input
    n, k = map(int, input().split())
    dice_values = list(map(int, input().split()))

    # Calculate the maximum expected sum
    maximum_expected_sum = get_maximum_expected_sum(dice_values, k)

    # Print the result
    print(maximum_expected_sum)

if __name__ == '__main__':
    main()

