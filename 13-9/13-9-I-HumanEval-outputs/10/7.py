
def is_equal_to_sum_even(n: int) -> bool:
    
    if n < 4:
        return False
    even_numbers = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even_numbers.append(i)
    return len(even_numbers) == 4 and sum(even_numbers) == n

