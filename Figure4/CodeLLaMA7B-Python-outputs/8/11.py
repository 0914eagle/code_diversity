from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    return sum(numbers), (1 if not numbers else 1) * len(numbers)


if __name__ == "__main__":
    import do