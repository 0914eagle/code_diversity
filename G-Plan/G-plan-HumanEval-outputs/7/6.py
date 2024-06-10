
def is_nested(string: str) -> bool:
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
    return not stack

if __name__ == "__main__":
    test_cases = [
        '[[]]',
        '[]]]]]]][[[[[]',
        '[][]',
        '[]',
        '[[][]]',
        '[[]][['
    ]
    for test in test_cases:
        print(is_nested(test))
