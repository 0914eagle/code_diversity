
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    notes = []
    for note in music_string.split():
        if note == 'o':
            notes.append(4)
        elif note == 'o|':
            notes.append(2)
        elif note == '.|':
            notes.append(1)
        else:
            raise ValueError(f"Invalid note: {note}")
    return notes

