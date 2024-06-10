
def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

brackets = input()
print(correct_bracketing(brackets))
