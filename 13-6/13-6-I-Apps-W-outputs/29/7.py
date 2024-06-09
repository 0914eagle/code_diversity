
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in non-decreasing order of beauty
    playlist.sort(key=lambda x: x[1])
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Initialize the total length of the selected songs to 0
    total_length = 0
    # Iterate through the playlist
    for song in playlist:
        # Check if the song is not already selected
        if song[0] not in selected_songs:
            # Add the length of the song to the total length
            total_length += song[0]
            # Add the beauty of the song to the maximum pleasure
            max_pleasure += song[1]
            # Add the song to the set of selected songs
            selected_songs.add(song[0])
        # Check if we have selected k songs
        if len(selected_songs) == k:
            # Break out of the loop
            break
    # Return the maximum pleasure
    return max_pleasure * total_length

