
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in descending order of beauty
    playlist.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    maximum_pleasure = 0
    # Iterate through the first k songs in the playlist
    for i in range(k):
        # Calculate the pleasure of listening to the current song
        pleasure = playlist[i][0] * playlist[i][1]
        # Update the maximum pleasure if the current pleasure is greater than the previous maximum pleasure
        if pleasure > maximum_pleasure:
            maximum_pleasure = pleasure
    # Return the maximum pleasure
    return maximum_pleasure

