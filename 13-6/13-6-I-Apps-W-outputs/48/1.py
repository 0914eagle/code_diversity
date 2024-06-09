
def get_min_coins(numbers):
    # Initialize the minimum number of coins to infinity
    min_coins = float('inf')
    # Loop through all possible combinations of signs
    for sign in itertools.product([1, -1], repeat=len(numbers)):
        # Calculate the product of the numbers with the current sign
        product = 1
        for i in range(len(numbers)):
            product *= numbers[i] * sign[i]
        # If the product is 1, we have found the minimum number of coins
        if product == 1:
            min_coins = min(min_coins, sum(sign))
    # Return the minimum number of coins
    return min_coins

def main():
    # Read the input
    n = int(input())
    numbers = list(map(int, input().split()))
    # Calculate the minimum number of coins
    min_coins = get_min_coins(numbers)
    # Print the result
    print(min_coins)

if __name__ == '__main__':
    main()

