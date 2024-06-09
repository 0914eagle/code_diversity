
def check_delimiters(L):
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    stack = []
    for i, char in enumerate(L):
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening[closing.index(char)] != stack[-1]:
                return char, i
            else:
                stack.pop()
    return "ok so far", -1

