
def sort_numbers(numbers: str) -> str:
    
    numbers_list = numbers.split()
    numbers_sorted = sorted(numbers_list)
    return " ".join(numbers_sorted)

