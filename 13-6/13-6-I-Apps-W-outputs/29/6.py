
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in descending order of beauty
    playlist.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Initialize the total length of the selected songs to 0
    total_length = 0
    # Iterate through the playlist and select the k songs with the highest beauty
    for i in range(k):
        # Add the length and beauty of the current song to the total length and maximum pleasure
        total_length += playlist[i][0]
        max_pleasure += playlist[i][1]
    # Return the maximum pleasure multiplied by the total length
    return max_pleasure * total_length
