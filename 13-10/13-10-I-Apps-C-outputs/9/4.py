
def get_tubes(tube_lengths, L1, L2):
    # Sort the tube lengths in non-decreasing order
    tube_lengths.sort()
    
    # Initialize the maximum total length of air that can be avoided to 0
    max_total_length = 0
    
    # Iterate over all possible pairs of tubes
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            # Calculate the total length of the first two tubes
            total_length1 = tube_lengths[i] + tube_lengths[j]
            
            # Check if the total length of the first two tubes is less than or equal to L1
            if total_length1 <= L1:
                # Calculate the total length of the last two tubes
                total_length2 = L1 - total_length1 + L2
                
                # Check if the total length of the last two tubes is less than or equal to L2
                if total_length2 <= L2:
                    # Calculate the maximum total length of air that can be avoided
                    max_total_length = max(max_total_length, total_length1 + total_length2)
    
    # Return the maximum total length of air that can be avoided
    return max_total_length

def main():
    # Read the input from stdin
    L1, L2, N = map(int, input().split())
    tube_lengths = list(map(int, input().split()))
    
    # Call the get_tubes function and print the result
    print(get_tubes(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

