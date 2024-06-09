
def sort_mobile_numbers(numbers):
    sorted_numbers = sorted(numbers, key=lambda x: x.strip('+91').strip('91').strip('0'))
    return ['+91 ' + x for x in sorted_numbers]

