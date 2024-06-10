
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string

    return longest_str

# Test cases
if __name__ == "__main__":
    input_strings = input().strip().split()
    result = longest(input_strings)
    print(result)
