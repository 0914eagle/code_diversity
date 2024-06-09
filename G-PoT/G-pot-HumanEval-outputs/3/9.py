
def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    max_negative = None
    min_positive = None

    for num in lst:
        if num < 0 and (max_negative is None or num > max_negative):
            max_negative = num
        elif num > 0 and (min_positive is None or num < min_positive):
            min_positive = num

    return max_negative, min_positive
