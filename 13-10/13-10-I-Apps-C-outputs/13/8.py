
def get_combinations(n, k):
    # Calculate the binomial coefficient
    result = 1
    for i in range(k):
        result = result * (n - i) / (i + 1)
    return result

def get_average_number_of_visitors(n, a, p):
    # Calculate the total number of possible combinations
    total_combinations = get_combinations(n, n)
    
    # Initialize the number of visitors variable
    num_visitors = 0
    
    # Iterate over all possible combinations
    for combination in itertools.permutations(range(1, n + 1)):
        # Calculate the sum of sizes of the guests in the combination
        size_sum = sum(a[i - 1] for i in combination)
        
        # Check if the sum of sizes is less than or equal to the table length
        if size_sum <= p:
            # Increment the number of visitors
            num_visitors += 1
    
    # Return the average number of visitors
    return num_visitors / total_combinations

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    p = int(input())
    
    # Calculate the average number of visitors
    average_number_of_visitors = get_average_number_of_visitors(n, a, p)
    
    # Print the result
    print(average_number_of_visitors)

if __name__ == '__main__':
    main()

