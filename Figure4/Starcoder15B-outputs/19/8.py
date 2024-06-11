from typing import List


def sort_numbers(numbers: str) -> str:
    
    # TODO: Implement this function
    return ' '.join(sorted(numbers.split(), key=lambda x: int(x.replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9'))))


if