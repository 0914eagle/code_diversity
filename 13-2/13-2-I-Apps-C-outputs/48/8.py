
def f1(n, k):
    # Sort the shows by their start time
    shows = sorted(zip(x, y), key=lambda x: x[0])
    
    # Initialize the number of recorded shows to 0
    recorded_shows = 0
    
    # Iterate through the shows and record them if possible
    for i in range(n):
        # Check if the current show can be recorded
        if recorded_shows < k:
            # Record the show and increment the number of recorded shows
            recorded_shows += 1
    
    # Return the number of recorded shows
    return recorded_shows

