
def get_combinations(n, k):
    # Calculate the binomial coefficient (n choose k)
    result = 1
    for i in range(k):
        result = result * (n - i) / (i + 1)
    return result

def get_number_of_ways(n, k, lamps):
    # Initialize the number of ways to 0
    number_of_ways = 0
    
    # Iterate over all possible combinations of lamps
    for combination in combinations(lamps, k):
        # Check if all lamps in the combination are turned on at the same time
        if all(lamp[0] <= lamp[1] for lamp in combination):
            number_of_ways += 1
    
    # Return the number of ways modulo 998244353
    return number_of_ways % 998244353

def main():
    # Read the input
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append((l, r))
    
    # Call the function to get the number of ways
    number_of_ways = get_number_of_ways(n, k, lamps)
    
    # Print the result
    print(number_of_ways)

if __name__ == '__main__':
    main()

