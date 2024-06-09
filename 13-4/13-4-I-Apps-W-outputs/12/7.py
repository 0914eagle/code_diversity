
def get_max_melody_length(notes):
    # Sort the notes in ascending order
    sorted_notes = sorted(notes)

    # Initialize variables to keep track of the maximum length and the current length
    max_length = 0
    current_length = 0

    # Iterate through the sorted notes
    for i in range(len(sorted_notes)):
        # If the current note is congruent to the previous note modulo 7, increase the current length by 1
        if i > 0 and sorted_notes[i] % 7 == sorted_notes[i-1] % 7:
            current_length += 1
        # If the current length is greater than the maximum length, update the maximum length
        elif current_length > max_length:
            max_length = current_length
        # Reset the current length to 1 if the current note is not congruent to the previous note modulo 7
        else:
            current_length = 1

    # Return the maximum length
    return max_length

