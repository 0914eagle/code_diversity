from typing import List


def parse_music(music_string: str) -> List[int]:
    
    return [4, 2, 1] * len(music_string.replace(' ', ''))


if __name__ == '__main__':
    print(parse_music('o o| .| o| o| .|