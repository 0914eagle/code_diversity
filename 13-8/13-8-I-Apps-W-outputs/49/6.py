
def is_rbs(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif char == "[":
            stack.append(char)
        elif char == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
        elif char == "{":
            stack.append(char)
        elif char == "}":
            if not stack or stack[-1] != "{":
                return False
            stack.pop()
        elif char == "<":
            stack.append(char)
        elif char == ">":
            if not stack or stack[-1] != "<":
                return False
            stack.pop()
    return not stack

def get_min_replaces(s):
    stack = []
    count = 0
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                stack.append(char)
                count += 1
            else:
                stack.pop()
        elif char == "[":
            stack.append(char)
        elif char == "]":
            if not stack or stack[-1] != "[":
                stack.append(char)
                count += 1
            else:
                stack.pop()
        elif char == "{":
            stack.append(char)
        elif char == "}":
            if not stack or stack[-1] != "{":
                stack.append(char)
                count += 1
            else:
                stack.pop()
        elif char == "<":
            stack.append(char)
        elif char == ">":
            if not stack or stack[-1] != "<":
                stack.append(char)
                count += 1
            else:
                stack.pop()
    return count

def main():
    s = input()
    if is_rbs(s):
        print(0)
    else:
        print(get_min_replaces(s))

if __name__ == "__main__":
    main()

