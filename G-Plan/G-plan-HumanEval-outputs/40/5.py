
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
            if char == '(':
                if current_group:
                    groups.append(current_group)
                current_group = "("
            elif char == ')':
                current_group += ")"
                groups.append(current_group)
                current_group = ""
        if current_group:
            groups.append(current_group)
        return groups

    paren_string = paren_string.replace(" ", "")
    groups = extract_groups(paren_string)
    result = [group for group in groups if is_balanced(group)]
    return result

# Test the function
input_string = input().strip()
result = separate_paren_groups(input_string)
print(result)
