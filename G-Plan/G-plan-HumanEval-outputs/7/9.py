
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
    input_string = input().strip()
    print(is_nested(input_string))
