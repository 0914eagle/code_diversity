
from typing import List

def is_balanced_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def match_parens(lst: List[str]) -> str:
    concatenated = lst[0] + lst[1]
    if is_balanced_parentheses(concatenated):
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    input_strings = input().strip().split()
    result = match_parens(input_strings)
    print(result)
