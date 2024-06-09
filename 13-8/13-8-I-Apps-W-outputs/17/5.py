
def get_maximum_clique_size(A):
    # Initialize a dictionary to store the divisibility relationships
    divisibility = {}
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] % A[j] == 0 or A[j] % A[i] == 0:
                divisibility[(A[i], A[j])] = True
            else:
                divisibility[(A[i], A[j])] = False
    
    # Initialize a set to store the maximum clique
    max_clique = set()
    
    # Iterate through the dictionary and find the maximum clique
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if divisibility[(A[i], A[j])] and A[i] not in max_clique and A[j] not in max_clique:
                max_clique.add(A[i])
                max_clique.add(A[j])
                break
    
    return len(max_clique)

