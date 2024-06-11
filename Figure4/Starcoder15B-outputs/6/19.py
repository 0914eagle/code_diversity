from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    return [max(len(list(g)) for _, g in groupby(s, key=lambda x: x == '(')) for s in paren_string.split()]
/tests/test_parse_nested_parens.py
from unittest import TestCase

from src.parse_nested_parens import parse_nested_parens


class