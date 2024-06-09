
def solve(a):
    # Calculate the sum of the elements in the array
    sum = 0
    for i in a:
        sum += i
    
    # Check if the sum is odd
    if sum % 2 == 1:
        return "YES"
    else:
        return "NO"

