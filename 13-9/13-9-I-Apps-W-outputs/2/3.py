
def get_name(N, P, A, B):
    # Sort the list of even integers
    P.sort()
    
    # Find the closest even integer to each odd integer in the range [A, B]
    closest = {}
    for i in range(A, B+1, 2):
        diff = [abs(i - j) for j in P]
        closest[i] = min(diff)
    
    # Return the odd integer with the maximum distance to the closest even integer
    return max(closest, key=closest.get)

