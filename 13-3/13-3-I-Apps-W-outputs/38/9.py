
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
        elif c == 'D':
            down += 1
    
    # Check if the string can be edited to end at the origin
    if left == right and up == down:
        return -1
    
    # Calculate the minimum number of edits required
    edits = 0
    if left > right:
        edits += left - right
    elif right > left:
        edits += right - left
    if up > down:
        edits += up - down
    elif down > up:
        edits += down - up
    
    return edits

