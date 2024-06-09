
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in descending order of beauty
    playlist.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Initialize the total length of the selected songs to 0
    total_length = 0
    # Iterate through the playlist and select the k songs with the highest beauty
    for i in range(k):
        # Calculate the pleasure of the current song
        pleasure = playlist[i][1] * (total_length + playlist[i][0])
        # Update the maximum pleasure if the current pleasure is higher
        max_pleasure = max(max_pleasure, pleasure)
        # Update the total length of the selected songs
        total_length += playlist[i][0]
    # Return the maximum pleasure
    return max_pleasure

