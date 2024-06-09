
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in descending order of beauty
    playlist.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    maximum_pleasure = 0
    # Initialize the total length of the songs to 0
    total_length = 0
    # Iterate through the first k songs in the playlist
    for i in range(k):
        # Add the length of the current song to the total length
        total_length += playlist[i][0]
        # If the total length is greater than the maximum pleasure, update the maximum pleasure
        if total_length > maximum_pleasure:
            maximum_pleasure = total_length
    # Return the maximum pleasure
    return maximum_pleasure

