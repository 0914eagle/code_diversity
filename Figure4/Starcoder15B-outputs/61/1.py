def correct_bracketing(brackets: str):
    
    # TODO: implement this function
    # Hint: use a stack
    stack = Stack()
    for bracket in brackets:
        if bracket == '(':
            stack.push(bracket)
        elif bracket == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


