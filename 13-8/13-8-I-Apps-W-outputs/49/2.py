
def is_rbs(s):
    stack = []
    for char in s:
        if char == "(" or char == "[" or char == "<" or char == "{":
            stack.append(char)
        else:
            if not stack or stack[-1] != match(char):
                return False
            stack.pop()
    return not stack

def match(char):
    if char == ")":
        return "("
    elif char == "]":
        return "["
    elif char == "}":
        return "{"
    else:
        return "<"

def get_min_replaces(s):
    stack = []
    count = 0
    for char in s:
        if char == "(" or char == "[" or char == "<" or char == "{":
            stack.append(char)
        else:
            if not stack or stack[-1] != match(char):
                stack.append(match(char))
                count += 1
            stack.pop()
    return count

def solve(s):
    if is_rbs(s):
        return "0"
    else:
        return str(get_min_replaces(s))

