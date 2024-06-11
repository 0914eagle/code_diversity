def correct_bracketing(brackets: str):
    
    # TODO: implement this function
    # Hint: use a stack
    # Hint: use a for loop to iterate through the string
    # Hint: use a while loop to keep popping from the stack until it is empty
    # Hint: use a counter to keep track of the number of opening brackets
    # Hint: use a counter to keep track of the number of closing brackets
    # Hint: if the number of opening brackets is not equal to the number of closing brackets, return False
    # Hint: if the stack is not empty at the end of the loop, return False
    # Hint: if the number of opening brackets is equal to the number of closing brackets, return True
    # Hint: if the stack is empty at the end of the loop, return True
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


if