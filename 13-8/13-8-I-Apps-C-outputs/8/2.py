
def get_longest_exploration_sequence(array, d, m):
    # Initialize variables
    n = len(array)
    visited = [False] * n
    longest_sequence = 0
    current_sequence = 0
    current_position = 0
    
    # Iterate through the array
    for i in range(n):
        # If the current position has not been visited, visit it and update the sequence
        if not visited[i]:
            visited[i] = True
            current_sequence += 1
            current_position = i
            
            # While there is a next position that is within the bounds and has a difference in value less than or equal to m, visit it and update the sequence
            while current_position + d < n and abs(array[current_position] - array[current_position + d]) <= m:
                current_sequence += 1
                current_position += d
                visited[current_position] = True
            
            # If the current sequence is longer than the longest sequence, update the longest sequence
            if current_sequence > longest_sequence:
                longest_sequence = current_sequence
        
    # Return the longest sequence
    return longest_sequence

def main():
    # Read the input
    n, d, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    # Call the function and print the result
    result = get_longest_exploration_sequence(array, d, m)
    print(result)

if __name__ == '__main__':
    main()

