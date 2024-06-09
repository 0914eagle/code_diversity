
def get_max_triples(n: int) -> int:
    
    # Initialize an empty list to store the results
    triples = []

    # Iterate through the array
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # Check if the sum of the current triple is divisible by 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # If it is, add the triple to the list of results
                    triples.append((a[i], a[j], a[k]))

    # Return the number of triples found
    return len(triples)

