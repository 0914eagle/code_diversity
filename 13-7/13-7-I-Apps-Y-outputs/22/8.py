
def stable_sort(attributes, songs, sort_commands):
    # Initialize the sorted songs list
    sorted_songs = songs

    # Loop through each sort command
    for command in sort_commands:
        # Sort the songs by the current attribute
        sorted_songs = sorted(sorted_songs, key=lambda x: x[attributes.index(command)])

    return sorted_songs

