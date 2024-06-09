
def solve(r, b, k):
    # Calculate the maximum number of planks that can be painted with the given conditions
    max_planks = (10**100 - 1) // (r * b)
    
    # Check if the number of planks is divisible by k
    if max_planks % k == 0:
        return "REBEL"
    else:
        return "OBEY"

