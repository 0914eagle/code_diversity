
def common(l1: List[int], l2: List[int]) -> List[int]:
    
    return sorted(list(set(l1) & set(l2)))
