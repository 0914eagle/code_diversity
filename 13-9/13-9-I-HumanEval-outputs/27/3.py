
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.split()
    return [note_values[note] for note in notes]

