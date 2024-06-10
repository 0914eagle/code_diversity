
def get_tubes(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # Initialize the total length of air to avoid as 0
    total_length = 0
    
    # Loop through the tube lengths and find two pairs that add up to L1 and L2
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            if tube_lengths[i] + tube_lengths[j] <= L1 and tube_lengths[i+1] + tube_lengths[j+1] <= L2:
                # If a pair is found, add their lengths to the total length of air to avoid
                total_length += tube_lengths[i] + tube_lengths[j] + tube_lengths[i+1] + tube_lengths[j+1]
                break
    
    # If a pair is not found, return the word "Impossible"
    if total_length == 0:
        return "Impossible"
    else:
        return total_length

def main():
    # Read the input
    L1, L2, N = map(int, input().split())
    tube_lengths = list(map(int, input().split()))
    
    # Call the get_tubes function and print the result
    print(get_tubes(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

