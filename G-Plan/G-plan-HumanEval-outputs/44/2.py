
from typing import Dict
from collections import Counter

def histogram(test: str) -> Dict[str, int]:
    counts = Counter(test.split())
    max_count = max(counts.values(), default=0)
    return {letter: count for letter, count in counts.items() if count == max_count}

if __name__ == "__main__":
    test_input = input().strip()
    result = histogram(test_input)
    print(result)
