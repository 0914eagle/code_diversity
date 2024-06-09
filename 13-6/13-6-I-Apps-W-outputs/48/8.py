
def get_min_coins(numbers):
    # Initialize the minimum number of coins to infinity
    min_coins = float('inf')
    
    # Loop through all possible combinations of adding/subtracting 1 from each number
    for i in range(2**len(numbers)):
        # Convert the binary string to a list of 0s and 1s
        combination = [int(x) for x in bin(i)[2:]]
        
        # Initialize the product of the numbers to 1
        product = 1
        
        # Loop through the numbers and update the product based on the current combination
        for j in range(len(numbers)):
            if combination[j] == 0:
                product *= numbers[j]
            else:
                product *= numbers[j] + 1
        
        # If the product is equal to 1, update the minimum number of coins
        if product == 1:
            min_coins = min(min_coins, sum(combination))
    
    return min_coins

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_min_coins(numbers))

if __name__ == '__main__':
    main()

