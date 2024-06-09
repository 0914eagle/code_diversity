
def sort_and_print_mobile_numbers(numbers):
    formatted_numbers = []
    for number in numbers:
        number = number.strip()
        if number.startswith("+91"):
            formatted_numbers.append(number[2:])
        elif number.startswith("91"):
            formatted_numbers.append(number[1:])
        elif number.startswith("0"):
            formatted_numbers.append(number)
        else:
            formatted_numbers.append("+91 " + number)
    return sorted(formatted_numbers)

