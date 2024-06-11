def next_smallest(lst):
    
    if not lst:
        return None
    lst.sort()
    return lst[1]

# Tests
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None
