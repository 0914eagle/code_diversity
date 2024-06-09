
def sort_even(l: List[int]) -> List[int]:
    even_indices = sorted([num for idx, num in enumerate(l) if idx % 2 == 0])
    result = l.copy()
    for idx, num in enumerate(l):
        if idx % 2 == 0:
            result[idx] = even_indices.pop(0)
    return result
