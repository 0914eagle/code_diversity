
def generate_integers(a: int, b: int) -> List[int]:
    
    return [num for num in range(a, b + 1) if num % 2 == 0]
