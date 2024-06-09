
def get_max_cuts(sequence, budget):
    # Initialize variables
    n = len(sequence)
    odd_count = 0
    even_count = 0
    cost = 0
    max_cuts = 0
    
    # Iterate through the sequence
    for i in range(n):
        # Check if the current element is odd or even
        if sequence[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        # Check if the current element is the last element in the sequence
        if i == n - 1:
            # Check if the total cost of the cuts is less than or equal to the budget
            if cost <= budget:
                # Increment the maximum number of cuts
                max_cuts += 1
        
        # Check if the current element is not the last element in the sequence
        else:
            # Calculate the cost of the current cut
            cost += abs(sequence[i] - sequence[i + 1])
        
            # Check if the total cost of the cuts is less than or equal to the budget
            if cost <= budget:
                # Increment the maximum number of cuts
                max_cuts += 1
    
    # Return the maximum number of cuts
    return max_cuts

def main():
    # Read the input
    n, budget = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    # Get the maximum number of cuts
    max_cuts = get_max_cuts(sequence, budget)
    
    # Print the maximum number of cuts
    print(max_cuts)

if __name__ == '__main__':
    main()

