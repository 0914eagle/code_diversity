from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    seen = set()
    return [n for n in numbers if n not in seen and not seen.add(n)]


if __name__ == "__main__":
    import doctest

   