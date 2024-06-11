def correct_bracketing(brackets: str):
    

    if len(brackets) % 2 != 0:
        return False

    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
   