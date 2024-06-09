
def solve(N):
    # Initialize the permutation as a list of numbers from 1 to N
    permutation = list(range(1, N+1))
    
    # Iterate through the permutation and find the first index where p_i != i
    for i in range(N):
        if permutation[i] != i+1:
            break
    
    # If we reach the end of the permutation without finding a match, return "NO"
    if i == N-1:
        return "NO"
    
    # Otherwise, find the next index where p_i & i == 0
    for j in range(i+1, N):
        if permutation[j] & (j+1) == 0:
            break
    
    # If we reach the end of the permutation without finding a match, return "NO"
    if j == N-1:
        return "NO"
    
    # Otherwise, swap the values at indices i and j to create the first permutation
    permutation[i], permutation[j] = permutation[j], permutation[i]
    
    # Create the second permutation by swapping the values at indices i and N
    permutation[i], permutation[N] = permutation[N], permutation[i]
    
    # Return the permutations as a list of space-separated strings
    return "YES\n" + " ".join(str(x) for x in permutation)

