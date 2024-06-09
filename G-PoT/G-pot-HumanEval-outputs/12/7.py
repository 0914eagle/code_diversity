
def add_elements(arr: List[int], k: int) -> int:
    
    sum_elements = 0
    for num in arr[:k]:
        if 10 <= num < 100:
            sum_elements += num
    return sum_elements
