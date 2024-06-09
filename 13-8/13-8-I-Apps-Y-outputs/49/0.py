
def solve(a):
    # Calculate the sum of the elements in the array
    sum_of_elements = sum(a)
    
    # Check if the sum is odd
    if sum_of_elements % 2 == 1:
        return "YES"
    
    # Check if there is a pair of indices with the same value
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return "YES"
    
    # If none of the above conditions are met, return "NO"
    return "NO"

