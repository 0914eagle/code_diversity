
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    note_values = {"o": 4, "o|": 2, ".|": 1}
    notes = []
    for note in music_string.split():
        notes.append(note_values[note])
    return notes

