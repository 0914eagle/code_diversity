
def get_min_coins(numbers):
    # Initialize the minimum number of coins to infinity
    min_coins = float('inf')
    
    # Loop through all possible signs
    for sign in ['+', '-']:
        # Initialize the current product to 1
        product = 1
        
        # Loop through all numbers
        for i in range(len(numbers)):
            # If the current number is not 0, add or subtract 1 from it
            if numbers[i] != 0:
                if sign == '+':
                    numbers[i] += 1
                else:
                    numbers[i] -= 1
            
            # Multiply the current product by the current number
            product *= numbers[i]
        
        # If the current product is 1, update the minimum number of coins
        if product == 1:
            min_coins = min(min_coins, len(numbers))
    
    # Return the minimum number of coins
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

