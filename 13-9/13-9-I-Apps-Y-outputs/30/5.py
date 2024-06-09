
def sort_phone_numbers(numbers):
    return sorted(numbers, key=lambda x: x.strip("+91").strip("91").strip("0"))

