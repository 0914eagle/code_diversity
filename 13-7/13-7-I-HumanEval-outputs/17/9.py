
def get_max_triples(n: int) -> int:
    
    # Initialize an empty list to store the triples
    triples = []
    
    # Iterate over the array
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # Check if a[i] + a[j] + a[k] is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # If it is, add the triple to the list of triples
                    triples.append((a[i], a[j], a[k]))
    
    # Return the length of the list of triples
    return len(triples)

