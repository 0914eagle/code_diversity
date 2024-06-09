
def check_delimiters(L):
    opening_delimiters = ["(", "[", "{"]
    closing_delimiters = [")", "]", "}"]
    stack = []
    for i, char in enumerate(L):
        if char in opening_delimiters:
            stack.append(char)
        elif char in closing_delimiters:
            if not stack or stack[-1] != opening_delimiters[closing_delimiters.index(char)]:
                return char, i
            else:
                stack.pop()
    if stack:
        return "ok so far", -1
    else:
        return "ok so far", -1

if __name__ == '__main__':
    L = input()
    print(check_delimiters(L))

