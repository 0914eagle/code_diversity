
def sort_even(l: List[int]) -> List[int]:
    even_indices = sorted([x for idx, x in enumerate(l) if idx % 2 == 0])
    result = [x if idx % 2 != 0 else even_indices.pop(0) for idx, x in enumerate(l)]
    return result
