
from typing import List

def is_balanced_parentheses(lst: List[str]) -> str:
    def is_balanced(s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    concatenated = lst[0] + lst[1]
    return 'Yes' if is_balanced(concatenated) else 'No'

if __name__ == "__main__":
    input_strings = input().strip().split()
    result = is_balanced_parentheses(input_strings)
    print(result)
