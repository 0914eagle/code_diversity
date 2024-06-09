
def stable_sort(my_tunes):
    # Initialize an empty dictionary to store the sorted songs
    sorted_songs = {}

    # Loop through each attribute in the input list
    for attribute in my_tunes:
        # Sort the songs by the current attribute, least to greatest
        sorted_songs[attribute] = sorted(my_tunes, key=lambda x: x[attribute])

    # Return the sorted songs in the order of the input list
    return [song for attribute in my_tunes for song in sorted_songs[attribute]]

