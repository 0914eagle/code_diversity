
def solve(k, n, heights):
    # Initialize a list to store the indices of the photos that need further investigation
    photos_to_investigate = []

    # Loop through each photo
    for i in range(k):
        # Check if the photo contains Alice and Bob
        if 1 in heights[i] and 3 in heights[i]:
            # Find the indices of Alice and Bob in the photo
            alice_index = heights[i].index(1)
            bob_index = heights[i].index(3)

            # Check if Alice is to the left of Bob
            if alice_index < bob_index:
                # Add the photo to the list of photos to investigate
                photos_to_investigate.append(i+1)

    # Return the list of photos to investigate
    return len(photos_to_investigate), sorted(photos_to_investigate)

