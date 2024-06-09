
def validate_delimiters(L):
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    stack = []
    for i, char in enumerate(L):
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening.index(stack.pop()) != closing.index(char):
                return char, i
    return "ok so far", -1

