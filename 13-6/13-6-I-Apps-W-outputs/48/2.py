
def get_min_coins(numbers):
    # Initialize the minimum number of coins to infinity
    min_coins = float('inf')
    # Loop through all possible combinations of numbers
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # Check if the product of the two numbers is equal to 1
            if numbers[i] * numbers[j] == 1:
                # If it is, return the minimum number of coins needed
                return 2
    # If no combination of numbers has a product of 1, return the minimum number of coins needed
    return min_coins

def main():
    # Read the input data
    n = int(input())
    numbers = list(map(int, input().split()))
    # Call the get_min_coins function and print the result
    print(get_min_coins(numbers))

if __name__ == '__main__':
    main()

