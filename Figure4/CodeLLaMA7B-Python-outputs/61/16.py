def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for c in brackets:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []


if __name__ == "__main__":
    import