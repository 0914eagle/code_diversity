
def get_distinct_ranks(N, K, a, b):
    # Initialize a dictionary to store the ranks
    ranks = {}
    
    # Loop through each assistant and its measurements
    for i in range(N):
        # Check if the assistant has already been ranked
        if i not in ranks:
            # Initialize the rank for the assistant
            ranks[i] = 0
            # Loop through the remaining assistants
            for j in range(i+1, N):
                # Check if the difference in measurements is greater than K
                if abs(a[i] - a[j]) > K or abs(b[i] - b[j]) > K:
                    # If the difference is greater than K, assign the same rank
                    ranks[j] = ranks[i]
    
    # Return the number of distinct ranks
    return len(set(ranks.values()))

def main():
    # Read the input
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Call the function to get the maximum number of distinct ranks
    result = get_distinct_ranks(N, K, a, b)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

