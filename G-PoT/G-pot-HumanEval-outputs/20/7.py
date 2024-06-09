
def sort_even(l: List[int]) -> List[int]:
    even_indices = sorted([val for idx, val in enumerate(l) if idx % 2 == 0])
    result = l.copy()
    for idx, val in enumerate(l):
        if idx % 2 == 0:
            result[idx] = even_indices.pop(0)
    return result
