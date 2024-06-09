
def get_distinct_modulo_42(numbers):
    distinct_modulo_42 = set()
    for number in numbers:
        distinct_modulo_42.add(number % 42)
    return len(distinct_modulo_42)

