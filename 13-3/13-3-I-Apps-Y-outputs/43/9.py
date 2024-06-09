
import re

def is_valid_roman_numeral(roman_numeral):
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, roman_numeral))

def main():
    roman_numeral = input("Enter a Roman numeral: ")
    print(is_valid_roman_numeral(roman_numeral))

if __name__ == '__main__':
    main()

