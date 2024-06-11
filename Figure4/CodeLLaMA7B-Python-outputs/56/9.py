def correct_bracketing(brackets: str):
    
    # Your code here
    # 1. count the number of opening and closing brackets
    # 2. return True if they are equal
    # 3. return False if they are not equal
    opening_brackets = 0
    closing_brackets = 0
    for bracket in brackets:
        if bracket == "<":
            opening_brackets += 1
        elif bracket == ">":
            closing_brackets += 1
    return opening_brackets == closing_brackets


print(correct_bracketing("<"))
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
