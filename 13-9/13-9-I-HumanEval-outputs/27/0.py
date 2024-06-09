
from typing import List

def parse_music(music_string: str) -> List[int]:
    
    notes = ['o', 'o|', '.|']
    note_values = [4, 2, 1]
    note_list = []
    for note in music_string.split():
        note_list.append(note_values[notes.index(note)])
    return note_list

