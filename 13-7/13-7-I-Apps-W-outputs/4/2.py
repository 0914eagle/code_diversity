
def solve(n, k, songs):
    # Sort the songs by beauty in descending order
    songs.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum pleasure to 0
    max_pleasure = 0
    # Loop through the first k songs
    for i in range(k):
        # Calculate the total length of the first i songs
        total_length = sum(map(lambda x: x[0], songs[:i + 1]))
        # Calculate the minimum beauty of the first i songs
        min_beauty = min(map(lambda x: x[1], songs[:i + 1]))
        # Calculate the pleasure of the first i songs
        pleasure = total_length * min_beauty
        # Update the maximum pleasure if necessary
        max_pleasure = max(max_pleasure, pleasure)
    # Return the maximum pleasure
    return max_pleasure

