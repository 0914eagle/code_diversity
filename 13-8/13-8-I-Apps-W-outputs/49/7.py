
def get_rbs(s):
    open_brackets = ["<", "{", "(", "["]
    close_brackets = [">", "}", ")", "]"]
    stack = []
    count = 0
    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or open_brackets.index(stack.pop()) != close_brackets.index(char):
                count += 1
    while stack:
        count += 1
        stack.pop()
    return "Impossible" if count % 2 else count // 2

