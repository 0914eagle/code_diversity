
def stable_sort(songs, attributes):
    # Initialize the sorted songs list
    sorted_songs = songs

    # Iterate through each attribute in the attributes list
    for attribute in attributes:
        # Sort the songs by the current attribute
        sorted_songs = sorted(sorted_songs, key=lambda x: x[attribute])

    return sorted_songs

