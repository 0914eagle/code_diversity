
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest_str):
            longest_str = s

    return longest_str

# Test cases
if __name__ == "__main__":
    strings = input().strip().split()
    result = longest(strings)
    print(result)
