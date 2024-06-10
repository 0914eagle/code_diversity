
from typing import List

def parse_music(music_string: str) -> List[int]:
    

    # Initialize an empty list to store the note durations
    note_durations = []

    # Iterate through each character in the input string
    for char in music_string:
        # Check if the current character is a whole note
        if char == 'o':
            # If it is, add 4 to the note durations list
            note_durations.append(4)
        # Check if the current character is a half note
        elif char == 'o|':
            # If it is, add 2 to the note durations list
            note_durations.append(2)
        # Check if the current character is a quarter note
        elif char == '.|':
            # If it is, add 1 to the note durations list
            note_durations.append(1)

    # Return the note durations list
    return note_durations

