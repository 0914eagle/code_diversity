
def solve(n, s, k, a):
    # Find the closest floor with an open restaurant
    for i in range(s, n+1):
        if i not in a:
            return i-s
    
    # If all floors above s are closed, find the closest floor with an open restaurant below s
    for i in range(s-1, -1, -1):
        if i not in a:
            return s-i
    
    # If all floors below s are closed, return 0
    return 0

