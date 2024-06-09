
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
    
    # Otherwise, swap the elements at indices i and j to form the first permutation
    permutation[i], permutation[j] = permutation[j], permutation[i]
    
    # Initialize the second permutation as a copy of the first permutation
    permutation2 = permutation[:]
    
    # Iterate through the permutation and find the first index where p_i != i
    for i in range(N):
        if permutation2[i] != i+1:
            break
    
    # If we reach the end of the permutation without finding a match, return "NO"
    if i == N-1:
        return "NO"
    
    # Otherwise, find the next index where p_i & i != 0
    for j in range(i+1, N):
        if permutation2[j] & (j+1) != 0:
            break
    
    # If we reach the end of the permutation without finding a match, return "NO"
    if j == N-1:
        return "NO"
    
    # Otherwise, swap the elements at indices i and j to form the second permutation
    permutation2[i], permutation2[j] = permutation2[j], permutation2[i]
    
    # Return "YES" and the two permutations
    return "YES\n" + " ".join(str(x) for x in permutation) + "\n" + " ".join(str(x) for x in permutation2)

