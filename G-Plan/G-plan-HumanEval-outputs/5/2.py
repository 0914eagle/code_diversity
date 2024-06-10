
def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

if __name__ == "__main__":
    brackets = input().strip()
    print(correct_bracketing(brackets))
