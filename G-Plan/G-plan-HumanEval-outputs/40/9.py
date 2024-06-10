
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    def extract_paren_groups(paren_string: str) -> List[str]:
        return re.findall(r'\([^()]*\)', paren_string)

    def remove_spaces(paren_string: str) -> str:
        return paren_string.replace(" ", "")

    paren_string = remove_spaces(paren_string)
    return extract_paren_groups(paren_string)

# Test the function
input_string = input().strip()
result = separate_paren_groups(input_string)
print(result)
