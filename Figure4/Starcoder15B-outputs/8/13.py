from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_ = 0
    product = 1
    for number in numbers:
        sum_ += number
        product *= number
    return sum_, product


if __name__ == '__main__':
    import doctest

    doctest.testmod()
/02_functions/02_01_seconds_per_day.py


seconds = int(input("Please enter the number of seconds: "))

if seconds > 86400:
    print("Invalid time")
else:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print(f"The duration of {hours} hours, {minutes} minutes, and {seconds} seconds.")
/02_functions/02_03_vowel_count.py


string = input("Please enter a string: ")

vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"There are {count} vowels in the string.")
/03_more_datatypes/3_tuples/03_19_list_to_