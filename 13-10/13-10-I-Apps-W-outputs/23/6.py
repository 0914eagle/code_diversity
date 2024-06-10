
def get_maximum_candies(n, k, M, D):
    # Initialize the maximum number of candies to 0
    max_candies = 0
    # Iterate from 1 to M
    for x in range(1, M + 1):
        # Calculate the number of candies given to each person
        num_candies = x * (k - 1) // k
        # Calculate the number of times each person receives candies
        num_times = x // D
        # Check if the number of candies is valid
        if num_candies <= n:
            # Calculate the number of candies received by Arkady
            num_candies_arkady = num_candies + (n - num_candies) % k
            # Check if the number of candies received by Arkady is greater than the current maximum
            if num_candies_arkady > max_candies:
                # Update the maximum number of candies
                max_candies = num_candies_arkady
    # Return the maximum number of candies
    return max_candies

def main():
    # Read the input data
    n, k, M, D = map(int, input().split())
    # Find the maximum number of candies Arkady can receive
    max_candies = get_maximum_candies(n, k, M, D)
    # Print the maximum number of candies
    print(max_candies)

if __name__ == '__main__':
    main()

