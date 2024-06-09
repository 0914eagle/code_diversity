
def solve(n, k, songs):
    # Sort the songs by beauty in descending order
    songs.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Loop through the first k songs
    for i in range(k):
        # Calculate the total pleasure of the current subset
        total_pleasure = sum(song[0] for song in songs[:i+1]) * songs[i][1]
        # Update the maximum pleasure if necessary
        max_pleasure = max(max_pleasure, total_pleasure)
    # Return the maximum pleasure
    return max_pleasure

