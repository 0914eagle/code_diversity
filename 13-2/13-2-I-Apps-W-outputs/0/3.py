
def count_problemsets(n, l, r, x, c):
    # Sort the difficulties in non-decreasing order
    c.sort()
    
    # Initialize the number of problemsets to 0
    num_problemsets = 0
    
    # Loop through all possible starting points for the problemset
    for i in range(n):
        # Get the current difficulty
        current_difficulty = c[i]
        
        # Check if the current difficulty is within the required range
        if l <= current_difficulty <= r:
            # Initialize the total difficulty of the problemset to the current difficulty
            total_difficulty = current_difficulty
            
            # Loop through the remaining problems
            for j in range(i+1, n):
                # Get the next difficulty
                next_difficulty = c[j]
                
                # Check if the next difficulty is within the required range
                if l <= next_difficulty <= r:
                    # Add the next difficulty to the total difficulty
                    total_difficulty += next_difficulty
                    
                    # Check if the total difficulty is within the required range
                    if total_difficulty >= l and total_difficulty <= r:
                        # Check if the difference in difficulty is within the required range
                        if abs(current_difficulty - next_difficulty) >= x:
                            # Increment the number of problemsets
                            num_problemsets += 1
    
    # Return the number of problemsets
    return num_problemsets

def main():
    # Read the input
    n, l, r, x = map(int, input().split())
    c = list(map(int, input().split()))
    
    # Call the count_problemsets function
    num_problemsets = count_problemsets(n, l, r, x, c)
    
    # Print the number of problemsets
    print(num_problemsets)

if __name__ == '__main__':
    main()

