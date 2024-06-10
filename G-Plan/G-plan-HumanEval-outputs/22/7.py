
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_str):
            longest_str = string

    return longest_str

# Test cases
if __name__ == "__main__":
    test_cases = [
        [],
        ['a', 'b', 'c'],
        ['a', 'bb', 'ccc']
    ]

    for test in test_cases:
        print(longest(test))
