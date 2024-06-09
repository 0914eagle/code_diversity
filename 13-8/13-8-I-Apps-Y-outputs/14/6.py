
def check_delimiters(L):
    L = L.strip()
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    stack = []
    for i, char in enumerate(L):
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening[closing.index(char)] != stack.pop():
                return char, i
    return "ok so far", -1

