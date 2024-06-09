
def solve(k, photos):
    # Initialize an empty list to store the indices of the photos that need further investigation
    photos_to_investigate = []

    # Iterate through each photo
    for i, photo in enumerate(photos):
        # Get the heights of the people in the photo
        heights = photo[1]

        # Check if Alice is taller than you
        if heights[0] > heights[1]:
            # Check if Bob is taller than both you and Alice
            if heights[2] > heights[0] and heights[2] > heights[1]:
                # Add the index of the photo to the list of photos to investigate
                photos_to_investigate.append(i+1)

    # Return the number of photos that need further investigation and the sorted indices of the photos to investigate
    return len(photos_to_investigate), sorted(photos_to_investigate)

