
def get_distinct_modulo_42(numbers):
    distinct_numbers = set()
    for number in numbers:
        distinct_numbers.add(number % 42)
    return len(distinct_numbers)

