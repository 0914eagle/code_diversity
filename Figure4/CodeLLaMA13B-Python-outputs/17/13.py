from typing import List


def parse_music(music_string: str) -> List[int]:
    
    beats = music_string.split()
    notes = []
    for beat in beats:
        if beat == 'o':
            notes.append(4)
        elif beat == 'o|':
            notes.append(2)
        elif beat == '.|':
            notes.append(1)
        else:
            raise ValueError('Invalid note')
    return notes


if