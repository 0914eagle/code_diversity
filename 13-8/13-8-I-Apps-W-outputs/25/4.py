
def solve(n, b):
    # Check if the sequence is already strictly increasing
    if all(b[i] < b[i+1] for i in range(n-1)):
        return "Yes\n" + " ".join(str(x) for x in b)
    
    # Find a permutation of the sequence that is strictly increasing
    permutation = find_permutation(b)
    if permutation is not None:
        return "Yes\n" + " ".join(str(x) for x in permutation)
    
    return "No"

def find_permutation(b):
    # Initialize the permutation with the first element of the sequence
    permutation = [b[0]]
    for i in range(1, len(b)):
        # Find the first element in the permutation that is greater than b[i]
        # and insert b[i] before it
        for j in range(len(permutation)):
            if permutation[j] > b[i]:
                permutation.insert(j, b[i])
                break
        else:
            # If we reach this point, it means that b[i] is the largest element
            # in the permutation, so we can add it to the end
            permutation.append(b[i])
    
    return permutation

