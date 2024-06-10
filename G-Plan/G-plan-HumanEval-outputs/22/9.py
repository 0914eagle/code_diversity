
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    longest_str = None
    for s in strings:
        if longest_str is None or len(s) > len(longest_str):
            longest_str = s
    return longest_str

# Test cases
if __name__ == "__main__":
    input_strings = input().strip().split()
    result = longest(input_strings)
    print(result)
