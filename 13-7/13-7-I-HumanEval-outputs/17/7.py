
def get_max_triples(n: int) -> int:
    

    # Initialize the array a with the given values
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # Initialize the count of valid triples to 0
    count = 0

    # Iterate over the array a
    for i in range(n - 2):
        # Iterate over the array a starting from the index i + 1
        for j in range(i + 1, n - 1):
            # Iterate over the array a starting from the index j + 1
            for k in range(j + 1, n):
                # Check if a[i] + a[j] + a[k] is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # Increment the count of valid triples
                    count += 1

    # Return the count of valid triples
    return count

