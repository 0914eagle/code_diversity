
def get_rbs(s):
    opening_brackets = ["{", "<", "[", "("]
    closing_brackets = ["}", ">", "]", ")"]
    stack = []
    count = 0
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                count += 1
                if count > 1:
                    return "Impossible"
    while stack:
        char = stack.pop()
        count += 1
        if count > 1:
            return "Impossible"
    return count

