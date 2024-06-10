
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

    result = []
    current_group = ''
    for char in paren_string:
        if char == ' ':
            continue
        current_group += char
        if is_balanced(current_group):
            result.append(current_group)
            current_group = ''
    
    return result

paren_string = input().strip()
print(separate_paren_groups(paren_string))
