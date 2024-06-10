
from typing import Dict
from collections import Counter

def histogram(test: str) -> Dict[str, int]:
    def parse_input(input_str: str) -> List[str]:
        return input_str.split()

    def count_occurrences(words: List[str]) -> Dict[str, int]:
        return dict(Counter(words))

    def find_max_count(occurrences: Dict[str, int]) -> int:
        return max(occurrences.values())

    def filter_max_occurrences(occurrences: Dict[str, int], max_count: int) -> Dict[str, int]:
        return {k: v for k, v in occurrences.items() if v == max_count}

    input_str = input()
    words = parse_input(input_str)
    occurrences = count_occurrences(words)
    max_count = find_max_count(occurrences)
    result = filter_max_occurrences(occurrences, max_count)
    
    return result

if __name__ == "__main__":
    print(histogram(""))
