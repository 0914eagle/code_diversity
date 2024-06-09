
def solve(A, B):
    # Check if A and B are both empty
    if not A and not B:
        return True
    
    # Check if one of the arrays is empty
    if not A or not B:
        return False
    
    # Check if the first element of A is less than the first element of B
    if A[0] < B[0]:
        return solve(A[1:], B)
    
    # Check if the first element of B is less than the first element of A
    if B[0] < A[0]:
        return solve(A, B[1:])
    
    # If none of the above conditions are met, return False
    return False

