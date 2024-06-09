
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in descending order of beauty
    playlist.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    maximum_pleasure = 0
    # Initialize the total length of the selected songs to 0
    total_length = 0
    # Iterate through the playlist
    for song in playlist:
        # Check if the song is not selected yet
        if song[1] > 0:
            # Increment the total length of the selected songs
            total_length += song[0]
            # Decrement the beauty of the selected song
            song[1] -= 1
            # Calculate the pleasure of the selected songs
            pleasure = total_length * song[1]
            # Check if the pleasure is greater than the maximum pleasure
            if pleasure > maximum_pleasure:
                # Update the maximum pleasure
                maximum_pleasure = pleasure
    # Return the maximum pleasure
    return maximum_pleasure

