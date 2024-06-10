
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    def is_opening_paren(char):
        return char == '('

    def is_closing_paren(char):
        return char == ')'

    result = []
    stack = []
    current_group = ""

    for char in paren_string:
        if char == ' ':
            continue

        if is_opening_paren(char):
            stack.append(char)
            if current_group:
                result.append(current_group)
                current_group = ""
        elif is_closing_paren(char):
            stack.pop()
            current_group += char
            if not stack:
                result.append(current_group)
                current_group = ""
        else:
            current_group += char

    return result

# Test the function with the provided example
print(separate_paren_groups('( ) (( )) (( )( ))'))
