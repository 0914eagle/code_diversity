
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for s in strings:
        if substring in s:
            result.append(s)
    return result

if __name__ == "__main__":
    strings = input().strip().split()
    substring = input().strip()
    result = filter_by_substring(strings, substring)
    print(result)
