
def get_longest_exploration_sequence(array, d, m):
    # Initialize a dictionary to store the longest exploration sequence for each index
    longest_sequence = {i: 1 for i in range(len(array))}
    
    # Iterate over the array
    for i in range(len(array)):
        # Get the current element and its value
        current_element = array[i]
        current_value = current_element[0]
        
        # Iterate over the next $D$ indices
        for j in range(1, d+1):
            # Check if the next index is within the bounds of the array
            if i+j < len(array):
                # Get the next element and its value
                next_element = array[i+j]
                next_value = next_element[0]
                
                # Check if the next value is within the maximum difference of $M$
                if abs(current_value - next_value) <= m:
                    # Update the longest exploration sequence for the current index
                    longest_sequence[i] = max(longest_sequence[i], longest_sequence[i+j] + 1)
    
    # Return the longest exploration sequence
    return max(longest_sequence.values())

def main():
    # Read the input
    n, d, m = map(int, input().split())
    array = [int(x) for x in input().split()]
    
    # Compute the longest exploration sequence
    longest_sequence = get_longest_exploration_sequence(array, d, m)
    
    # Print the result
    print(longest_sequence)

if __name__ == '__main__':
    main()

