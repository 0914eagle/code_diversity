
def get_tube_pairs(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # Initialize the total length of air to avoid
    total_length = 0
    
    # Loop through the tube lengths and find pairs that add up to L1 or L2
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            if tube_lengths[i] + tube_lengths[j] <= L1:
                total_length += tube_lengths[i] + tube_lengths[j]
                break
    
    # If no pairs add up to L1, return impossible
    if total_length == 0:
        return "Impossible"
    
    # Loop through the tube lengths and find pairs that add up to L2
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            if tube_lengths[i] + tube_lengths[j] <= L2:
                total_length += tube_lengths[i] + tube_lengths[j]
                break
    
    # If no pairs add up to L2, return impossible
    if total_length == 0:
        return "Impossible"
    
    # Return the total length of air to avoid
    return total_length

def main():
    # Read the input
    L1, L2, N = map(int, input().split())
    tube_lengths = list(map(int, input().split()))
    
    # Call the get_tube_pairs function and print the result
    print(get_tube_pairs(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

