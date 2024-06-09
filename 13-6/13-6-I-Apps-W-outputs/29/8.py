
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in descending order of beauty
    playlist.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Initialize the total length of the selected songs to 0
    total_length = 0
    # Iterate through the playlist and select the k songs with the highest beauty
    for i in range(k):
        # Calculate the total length of the selected songs
        total_length += playlist[i][0]
        # Calculate the maximum pleasure possible with the selected songs
        max_pleasure = max(max_pleasure, total_length * playlist[i][1])
    return max_pleasure
