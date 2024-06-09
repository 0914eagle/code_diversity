
def validate_delimiters(line):
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    stack = []
    for i, char in enumerate(line):
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening.index(stack.pop()) != closing.index(char):
                return char, i
    return "ok so far", -1

