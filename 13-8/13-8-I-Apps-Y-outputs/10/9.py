
def sort_and_print_phone_numbers(numbers):
    
    sorted_numbers = sorted(numbers)
    formatted_numbers = []
    for number in sorted_numbers:
        if len(number) == 10:
            formatted_numbers.append("+91 " + number[:5] + " " + number[5:])
        else:
            formatted_numbers.append(number)
    return formatted_numbers

