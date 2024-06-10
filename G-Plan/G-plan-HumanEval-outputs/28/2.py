
from typing import List

def is_balanced(paren_str: str) -> bool:
    stack = []
    for char in paren_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def match_parens(lst: List[str]) -> str:
    concat_str = lst[0] + lst[1]
    return 'Yes' if is_balanced(concat_str) else 'No'

if __name__ == "__main__":
    input_lst = input().strip().split()
    print(match_parens(input_lst))
