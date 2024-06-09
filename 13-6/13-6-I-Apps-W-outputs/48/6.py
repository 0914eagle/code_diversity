
def get_min_coins(numbers):
    # Initialize the minimum number of coins to infinity
    min_coins = float('inf')
    
    # Loop through all possible signs
    for sign in ['+', '-']:
        # Initialize the current product to 1
        product = 1
        
        # Loop through all numbers
        for number in numbers:
            # If the current number is not 0, add or subtract 1 from it based on the sign
            if number != 0:
                if sign == '+':
                    number += 1
                else:
                    number -= 1
            
            # Multiply the current product by the current number
            product *= number
        
        # If the current product is 1, return the current number of coins
        if product == 1:
            return len(numbers) - sum(number == 0 for number in numbers)
    
    # If no product is equal to 1, return the minimum number of coins
    return min_coins

def main():
    # Read the number of numbers and the numbers from stdin
    n = int(input())
    numbers = list(map(int, input().split()))
    
    # Call the get_min_coins function and print the result
    print(get_min_coins(numbers))

if __name__ == '__main__':
    main()

