
def get_max_triples(n: int) -> int:
    

    # Initialize the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]

    # Initialize the number of triples to 0
    num_triples = 0

    # Iterate over the array a
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if a[i] + a[j] + a[k] is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # Increment the number of triples
                    num_triples += 1

    # Return the number of triples
    return num_triples

