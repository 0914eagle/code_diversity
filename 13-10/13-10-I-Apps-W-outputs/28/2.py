
def get_min_days(n, k, weights):
    # Sort the weights in descending order
    weights.sort(reverse=True)
    # Initialize the number of days needed to collect all pebbles
    days = 0
    # Loop through the weights and add the current weight to the current pocket
    for i in range(n):
        days += weights[i] // k
        # If the current weight is not divisible by k, add an extra day
        if weights[i] % k != 0:
            days += 1
    return days

def main():
    # Read the input data
    n, k = map(int, input().split())
    weights = list(map(int, input().split()))
    # Calculate the minimum number of days needed to collect all pebbles
    days = get_min_days(n, k, weights)
    # Print the result
    print(days)

if __name__ == '__main__':
    main()

