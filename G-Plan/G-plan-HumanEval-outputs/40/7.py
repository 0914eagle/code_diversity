
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    def extract_paren_groups(paren_string: str) -> List[str]:
        groups = []
        current_group = ""
        for char in paren_string:
            if char == '(':
                current_group = ""
            elif char == ')':
                groups.append(current_group)
            else:
                current_group += char
        return groups

    return extract_paren_groups(paren_string.replace(" ", ""))

paren_string = input().strip()
result = separate_paren_groups(paren_string)
print(result)
