
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate through the characters in the input string
    for char in music_string:
        # Check if the character is 'o', which represents a whole note
        if char == 'o':
            # If it is, add 4 to the beats list
            beats.append(4)
        # Check if the character is 'o|', which represents a half note
        elif char == 'o|':
            # If it is, add 2 to the beats list
            beats.append(2)
        # Check if the character is '.|', which represents a quarter note
        elif char == '.|':
            # If it is, add 1 to the beats list
            beats.append(1)

    # Return the list of beats
    return beats

