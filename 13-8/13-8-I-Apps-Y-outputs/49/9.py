
def solve(a):
    # Calculate the sum of the elements in the array
    sum = 0
    for i in a:
        sum += i
    
    # Return "YES" if the sum is odd, otherwise return "NO"
    if sum % 2 == 1:
        return "YES"
    else:
        return "NO"

