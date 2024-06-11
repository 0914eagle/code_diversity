from typing import List


def parse_music(music_string: str) -> List[int]:
    
    return [4, 2, 1] * len(music_string.replace(' ', ''))


if