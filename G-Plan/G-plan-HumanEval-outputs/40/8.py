
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    def is_balanced(group: str) -> bool:
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack

    def extract_groups(paren_string: str) -> List[str]:
        groups = []
        current_group = ""
        for char in paren_string:
            if char == '(' or char == ')':
                current_group += char
            if char == ')' and is_balanced(current_group):
                groups.append(current_group)
                current_group = ""
        return groups

    return extract_groups(paren_string.replace(" ", ""))

paren_string = input()
result = separate_paren_groups(paren_string)
print(result)
