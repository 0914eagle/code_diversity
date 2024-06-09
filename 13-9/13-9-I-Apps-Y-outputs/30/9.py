
def sort_and_format_phone_numbers(numbers):
    formatted_numbers = []
    for number in numbers:
        number = number.strip()
        if number.startswith("+91"):
            number = number[3:]
        elif number.startswith("91"):
            number = number[2:]
        elif number.startswith("0"):
            number = number[1:]
        formatted_numbers.append("+91 " + number[:5] + " " + number[5:])
    return formatted_numbers

