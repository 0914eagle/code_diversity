
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
    return len(stack) == 0

def match_parens(lst: List[str]) -> str:
    concatenated = ''.join(lst)
    return 'Yes' if is_balanced_parentheses(concatenated) else 'No'

if __name__ == "__main__":
    lst = input().strip().split()
    result = match_parens(lst)
    print(result)
