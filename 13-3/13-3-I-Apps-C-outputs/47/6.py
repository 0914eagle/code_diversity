
def solve(L1, L2, N, tubes):
    # Sort the tubes in descending order
    tubes.sort(reverse=True)

    # Initialize the maximum total length of air that can be avoided
    max_length = 0

    # Iterate over all possible pairs of tubes
    for i in range(N):
        for j in range(i+1, N):
            # Check if the sum of the lengths of the first two tubes is less than or equal to L1
            if tubes[i] + tubes[j] <= L1:
                # Check if the sum of the lengths of the last two tubes is less than or equal to L2
                if tubes[i+1] + tubes[j+1] <= L2:
                    # Calculate the total length of air that can be avoided
                    length = tubes[i] + tubes[j] + tubes[i+1] + tubes[j+1]

                    # Update the maximum total length of air that can be avoided
                    max_length = max(max_length, length)

    # Return the maximum total length of air that can be avoided
    return max_length

