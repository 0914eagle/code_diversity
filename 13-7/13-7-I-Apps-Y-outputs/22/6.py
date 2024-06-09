
def stable_sort(songs, sort_attributes):
    # Initialize the sorted songs list
    sorted_songs = []

    # Iterate through the sort attributes
    for attribute in sort_attributes:
        # Sort the songs by the current attribute
        sorted_songs = sorted(songs, key=lambda x: x[attribute])

        # Append the sorted songs to the output list
        songs = sorted_songs

    # Return the sorted songs
    return sorted_songs

