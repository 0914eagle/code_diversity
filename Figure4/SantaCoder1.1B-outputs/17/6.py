from typing import List


def parse_music(music_string: str) -> List[int]:
    
    notes = []
    for char in music_string:
        if char == 'o':
            notes.append(4)
        elif char == 'o|':
            notes.append(2)
        elif char == '.|':
            notes.append(1)
        elif char == 'o|o':
            notes.append(1)
            notes.append(4)
    return notes


