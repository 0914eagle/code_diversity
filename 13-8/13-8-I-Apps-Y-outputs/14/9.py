
def validate_delimiters(line):
    opening_delimiters = ["(", "[", "{"]
    closing_delimiters = [")", "]", "}"]
    stack = []
    for i, char in enumerate(line):
        if char in opening_delimiters:
            stack.append(char)
        elif char in closing_delimiters:
            if not stack or stack[-1] != opening_delimiters[closing_delimiters.index(char)]:
                return char, i
            else:
                stack.pop()
    if stack:
        return stack[-1], len(line)
    return "ok so far", 0

