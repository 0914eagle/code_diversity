
import re

def is_roman_numeral(s):
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, s))

