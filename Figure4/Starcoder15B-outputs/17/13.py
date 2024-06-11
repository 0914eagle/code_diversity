from typing import List


def parse_music(music_string: str) -> List[int]:
    
    return [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
/02_functions/01_functions_basics/tests/test_01_functions_basics.py
import pytest

from solutions.01_functions_basics import (
    hello_world,
    hello_name,
    hello_name_with_