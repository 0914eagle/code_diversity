
def solve(s):
    n = len(s)
    for i in range(n):
        if s[i] == '?':
            s = s[:i] + '(' + s[i+1:]
    for i in range(n):
        if s[i] == '?':
            s = s[:i] + ')' + s[i+1:]
    for i in range(1, n):
        if s[:i] not in ['()', '(())', '((()))', '(((()))', '((((()))))']:
            return ':('
    return s

