
def get_max_triples(n: int) -> int:
    
    # Initialize the array with the given values
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # Initialize the count of valid triples to 0
    count = 0
    # Iterate over the array
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # Check if the sum of the current triple is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # Increment the count of valid triples
                    count += 1
    # Return the count of valid triples
    return count

