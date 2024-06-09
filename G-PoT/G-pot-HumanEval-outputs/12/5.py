
def add_elements(arr: List[int], k: int) -> int:
    
    total_sum = 0
    for num in arr[:k]:
        if 10 <= num < 100:
            total_sum += num
    return total_sum
