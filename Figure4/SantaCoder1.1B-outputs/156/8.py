def int_to_mini_roman(number):
    
    if number < 1 or number > 3999:
        raise ValueError("Number out of range")

    roman_numeral = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    return roman_numeral[number]


