from typing import List


def parse_music(music_string: str) -> List[int]:
    
    notes = []
    for char in music_string:
        if char == 'o':
            notes.append(4)
        elif char == 'o|':
            notes.append(2)
        elif char == '.|':
            notes.append(1)
    return notes


if __name__ == '__main__':
    import doctest
    doctest.testmod()