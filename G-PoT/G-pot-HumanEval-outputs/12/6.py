
def add_elements(arr: List[int], k: int) -> int:
    
    total = 0
    for num in arr[:k]:
        if 10 <= num < 100:
            total += num
    return total
