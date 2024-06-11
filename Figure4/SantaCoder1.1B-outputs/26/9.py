from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    return list(set(numbers))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
