
def sort_even(l: List[int]) -> List[int]:
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    sorted_values = sorted([l[i] for i in even_indices])
    result = l.copy()
    for i, val in zip(even_indices, sorted_values):
        result[i] = val
    return result
