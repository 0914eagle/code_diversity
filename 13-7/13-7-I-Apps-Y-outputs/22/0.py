
def stable_sort(attrs, songs, commands):
    # Initialize the output lists
    output_lists = []

    # Iterate over the commands
    for command in commands:
        # Find the index of the command in the attributes list
        command_index = attrs.index(command)

        # Sort the songs by the current command
        sorted_songs = sorted(songs, key=lambda x: x[command_index])

        # Add the sorted songs to the output lists
        output_lists.append(sorted_songs)

    # Return the output lists
    return output_lists

