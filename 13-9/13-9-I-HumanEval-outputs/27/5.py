
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    note_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.split()
    note_durations = [note_duration[note] for note in notes]
    return note_durations

