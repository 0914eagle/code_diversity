
def get_min_coins(numbers):
    # Initialize the minimum number of coins to infinity
    min_coins = float('inf')
    # Loop through all possible combinations of adding/subtracting 1
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            # Check if the product of the numbers is 1
            if np.prod(numbers) == 1:
                # If so, return the current number of coins
                return len(numbers) - 1
            # Add 1 to the current number
            numbers[i] += 1
            # Recursively call the function with the updated numbers
            min_coins = min(min_coins, get_min_coins(numbers))
            # Subtract 1 from the current number
            numbers[i] -= 1
            # Recursively call the function with the updated numbers
            min_coins = min(min_coins, get_min_coins(numbers))
    # Return the minimum number of coins
    return min_coins

def main():
    # Read the input
    n = int(input())
    numbers = list(map(int, input().split()))
    # Get the minimum number of coins
    min_coins = get_min_coins(numbers)
    # Print the result
    print(min_coins)

if __name__ == '__main__':
    main()

