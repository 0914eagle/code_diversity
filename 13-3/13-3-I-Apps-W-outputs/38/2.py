
def f1(s):
    # Initialize variables
    left, right, up, down = 0, 0, 0, 0
    for c in s:
        if c == 'L':
            left += 1
        elif c == 'R':
            right += 1
        elif c == 'U':
            up += 1
        else:
            down += 1
    
    # Check if the string can be edited to end at the origin
    if left != right or up != down:
        return -1
    
    # Count the minimum number of edits required
    edits = 0
    for i in range(len(s)):
        if s[i] == 'L' and s[i-1] == 'R':
            s = s[:i-1] + 'U' + s[i:]
            edits += 1
        elif s[i] == 'R' and s[i-1] == 'L':
            s = s[:i-1] + 'D' + s[i:]
            edits += 1
    
    return edits

