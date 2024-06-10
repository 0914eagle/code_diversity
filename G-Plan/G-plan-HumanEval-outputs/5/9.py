
def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    brackets = input().strip()
    print(correct_bracketing(brackets))
