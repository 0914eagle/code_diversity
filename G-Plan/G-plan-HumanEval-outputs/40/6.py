
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

# Test the function
input_string = input().strip()
result = separate_paren_groups(input_string)
print(result)
