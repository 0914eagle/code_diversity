from typing import List


def parse_music(music_string: str) -> List[int]:
    
    notes = []
    for note in music_string:
        if note == 'o':
            notes.append(4)
        elif note == 'o|':
            notes.append(2)
        elif note == '.|':
            notes.append(1)
        elif note == 'o o':
            notes.append(4)
            notes.append(2)
        elif note == 'o o|':
            notes.append(2)
            notes.append(1)
        elif note == '.| o':
            notes.append(1)
            notes.append(2)
        elif note == 'o o|.':
            notes.append(4)
            notes.append(2)
            notes.append(1)
        elif note == 'o o|.|':
            notes.append(2)
            notes.append(1)
            notes.append(2)
        elif note == '.| o|.':
            notes.append(1)
            notes.append(2)
            notes.append(1)
        elif note == 'o o|.|.':
            notes.append(4)
            notes.append(2)
            notes.append(1)
            notes.append(2)
        elif note == '.| o|.|.':
            notes.append(1)
            notes.append(2)
            notes.append(1)
            notes.append(2)
            notes.append(1)
    return notes


if __name__ == '__main__':
    import doctest
    doctest.testmod()
