
def get_max_clique(A):
    # Initialize a dictionary to store the divisibility relationships
    divisibility = {}
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] % A[j] == 0 or A[j] % A[i] == 0:
                divisibility[(A[i], A[j])] = True
            else:
                divisibility[(A[i], A[j])] = False
    
    # Find the maximum clique by iteratively adding vertices to the clique
    # and checking if the added vertex is connected to all the other vertices in the clique
    max_clique = []
    for i in range(len(A)):
        clique = [A[i]]
        for j in range(i+1, len(A)):
            if (A[i], A[j]) in divisibility and (A[j], A[i]) in divisibility:
                clique.append(A[j])
        if len(clique) > len(max_clique):
            max_clique = clique
    
    return len(max_clique)

