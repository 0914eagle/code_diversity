
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    note_list = []
    for note in music_string.split():
        note_list.append(note_values[note])
    return note_list

