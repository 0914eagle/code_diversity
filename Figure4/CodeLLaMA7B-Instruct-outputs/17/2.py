
from typing import List


def parse_music(music_string: str) -> List[int]:
    
    beat_map = {'o': 4, 'o|': 2, '.|': 1}
    beats: List[int] = []
    for char in music_string:
        if char in beat_map:
            beats.append(beat_map[char])
        else:
            beats.append(1)
    return beats

