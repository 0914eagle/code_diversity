
def solve(n, k, a):
    # Check if all elements are already equal to k
    if all(x == k for x in a):
        return "yes"
    
    # Check if the sum of all elements is even or odd
    if sum(a) % 2 == 0:
        # Even sum
        return "no"
    else:
        # Odd sum
        return "yes"

