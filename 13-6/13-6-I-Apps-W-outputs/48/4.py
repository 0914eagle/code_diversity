
def get_min_coins(numbers):
    # Initialize the minimum number of coins to infinity
    min_coins = float('inf')
    # Loop through all possible signs
    for sign in [-1, 1]:
        # Initialize the current product to 1
        product = 1
        # Loop through all numbers
        for number in numbers:
            # Calculate the current product
            product *= number + sign
        # If the current product is 1, return the minimum number of coins
        if product == 1:
            return min_coins
        # Otherwise, update the minimum number of coins
        min_coins = min(min_coins, abs(product - 1))
    # If no product is equal to 1, return the minimum number of coins
    return min_coins

def main():
    # Read the number of numbers and the numbers from stdin
    n = int(input())
    numbers = list(map(int, input().split()))
    # Get the minimum number of coins needed to make the product equal to 1
    min_coins = get_min_coins(numbers)
    # Print the minimum number of coins
    print(min_coins)

if __name__ == '__main__':
    main()

