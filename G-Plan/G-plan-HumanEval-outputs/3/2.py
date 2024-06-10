
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = [s for s in strings if substring in s]
    return result

if __name__ == "__main__":
    strings = input().strip().split()
    substring = input().strip()
    result = filter_by_substring(strings, substring)
    print(result)
