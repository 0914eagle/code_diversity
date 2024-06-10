
def find_longest_tubes(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # Initialize the longest tube lengths as the first two tubes
    longest_tubes = [tube_lengths[0], tube_lengths[1]]
    
    # Initialize the total length of the longest tubes as the sum of the first two tubes
    longest_length = sum(longest_tubes)
    
    # Iterate through the remaining tubes
    for tube in tube_lengths[2:]:
        # If the sum of the longest tubes and the current tube is less than or equal to L1, add the current tube to the longest tubes
        if longest_length + tube <= L1:
            longest_tubes.append(tube)
            longest_length += tube
    
    # If the sum of the longest tubes is greater than L2, return impossible
    if longest_length > L2:
        return "Impossible"
    
    # Return the sum of the longest tubes
    return longest_length

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = list(map(int, input().split()))
    print(find_longest_tubes(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

