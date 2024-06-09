
def solve(numbers):
    sorted_numbers = sorted(numbers)
    formatted_numbers = []
    for number in sorted_numbers:
        if number.startswith('+91'):
            formatted_numbers.append('+91 ' + number[3:])
        elif number.startswith('91'):
            formatted_numbers.append('+91 ' + number[2:])
        elif number.startswith('0'):
            formatted_numbers.append('+91 ' + number)
        else:
            formatted_numbers.append('+91 ' + number)
    return formatted_numbers

