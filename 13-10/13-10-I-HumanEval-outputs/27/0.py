
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    notes = []
    for note in music_string.split():
        notes.append(note_durations[note])

    return notes

