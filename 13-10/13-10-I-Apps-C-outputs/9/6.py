
def get_tubes_lengths(L1, L2, N):
    # Sort the tubes lengths in descending order
    tubes_lengths = sorted([int(input()) for _ in range(N)], reverse=True)
    # Initialize the maximum total length of air that can be avoided
    max_length = 0
    # Iterate over all possible pairs of tubes
    for i in range(N-1):
        for j in range(i+1, N):
            # Check if the sum of the first two tubes is at most L1 and the sum of the last two tubes is at most L2
            if tubes_lengths[i] + tubes_lengths[j] <= L1 and L1 + L2 - tubes_lengths[i] - tubes_lengths[j] <= L2:
                # Update the maximum total length of air that can be avoided
                max_length = max(max_length, tubes_lengths[i] + tubes_lengths[j] + L1 + L2 - tubes_lengths[i] - tubes_lengths[j])
    # Return the maximum total length of air that can be avoided
    return max_length

def main():
    # Read the input
    L1, L2, N = map(int, input().split())
    # Get the lengths of the tubes
    tubes_lengths = get_tubes_lengths(L1, L2, N)
    # Check if there are no two pairs of tubes fitting into the setup
    if tubes_lengths == 0:
        print("Impossible")
    # Otherwise, print the maximum total length of air that can be avoided
    else:
        print(tubes_lengths)

if __name__ == '__main__':
    main()

