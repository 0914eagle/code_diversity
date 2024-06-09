
def solve(playlist, k):
    # Sort the playlist by beauty
    playlist.sort(key=lambda x: x[1])
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Iterate over the first k songs
    for i in range(k):
        # Calculate the total pleasure for the current subset
        total_pleasure = sum(song[0] for song in playlist[:i+1]) * playlist[i][1]
        # Update the maximum pleasure if necessary
        max_pleasure = max(max_pleasure, total_pleasure)
    # Return the maximum pleasure
    return max_pleasure

