
def get_maximum_pleasure(playlist, k):
    # Sort the playlist in descending order of beauty
    playlist.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Initialize the total length of the selected songs to 0
    total_length = 0
    # Iterate through the playlist and select the songs
    for song in playlist:
        # Check if the song is not already selected
        if song[0] not in selected_songs:
            # Add the length and beauty of the song to the total length and maximum pleasure
            total_length += song[0]
            max_pleasure += song[1]
            # Add the song to the list of selected songs
            selected_songs.append(song[0])
        # Check if the total length of the selected songs is greater than or equal to k
        if len(selected_songs) >= k:
            # Break out of the loop
            break
    # Return the maximum pleasure
    return max_pleasure

