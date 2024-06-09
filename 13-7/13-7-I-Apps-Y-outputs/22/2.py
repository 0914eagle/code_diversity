
def stable_sort(songs, attributes):
    # Initialize the sorted list with the initial order of the songs
    sorted_songs = songs

    # Iterate through the list of attributes in the order they were given
    for attribute in attributes:
        # Sort the songs by the current attribute, using a stable sort algorithm
        sorted_songs = sorted(sorted_songs, key=lambda x: x[attribute])

    return sorted_songs

