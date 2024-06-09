
def sort_even(l: List[int]) -> List[int]:
    even_indices = sorted([num for idx, num in enumerate(l) if idx % 2 == 0])
    result = [num if idx % 2 != 0 else even_indices.pop(0) for idx, num in enumerate(l)]
    return result
