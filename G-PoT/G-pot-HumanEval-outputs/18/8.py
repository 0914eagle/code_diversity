
def common(l1: List[int], l2: List[int]) -> List[int]:
    
    common_elements = set(l1) & set(l2)
    return sorted(list(common_elements))
