
from typing import Dict
from collections import Counter

def histogram(test: str) -> Dict[str, int]:
    def count_letters(test: str) -> Dict[str, int]:
        return dict(Counter(test.split()))

    def find_max_count(letters_count: Dict[str, int]) -> int:
        return max(letters_count.values()) if letters_count else 0

    def filter_max_letters(letters_count: Dict[str, int], max_count: int) -> Dict[str, int]:
        return {letter: count for letter, count in letters_count.items() if count == max_count}

    letters_count = count_letters(test)
    max_count = find_max_count(letters_count)
    result = filter_max_letters(letters_count, max_count)
    
    return result

if __name__ == "__main__":
    test = input().strip()
    result = histogram(test)
    print(result)
