
def get_maximum_pleasure(playlist, k):
    # Sort the playlist by beauty
    playlist.sort(key=lambda x: x[1])
    # Initialize the maximum pleasure to 0
    maximum_pleasure = 0
    # Initialize the current pleasure to 0
    current_pleasure = 0
    # Iterate through the first k songs
    for i in range(k):
        # Add the length of the current song to the current pleasure
        current_pleasure += playlist[i][0]
        # Update the maximum pleasure if necessary
        maximum_pleasure = max(maximum_pleasure, current_pleasure)
    # Return the maximum pleasure
    return maximum_pleasure

