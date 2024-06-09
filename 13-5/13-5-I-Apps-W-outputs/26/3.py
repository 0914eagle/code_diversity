
def solve(s):
    n = len(s)
    for i in range(n):
        if s[i] == '?':
            s = s[:i] + '(' + s[i+1:]
    for i in range(n):
        if s[i] == '?':
            s = s[:i] + ')' + s[i+1:]
    for i in range(1, n):
        if s[:i] != '':
            if is_correct_parenthesis_sequence(s[:i]):
                return ':('
    return s

def is_correct_parenthesis_sequence(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

