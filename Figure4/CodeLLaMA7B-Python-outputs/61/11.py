def correct_bracketing(brackets: str):
    
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")":
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []


