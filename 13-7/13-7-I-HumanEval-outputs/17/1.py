
def get_max_triples(n: int) -> int:
    
    # Initialize an empty list to store the values of a
    a = []

    # Loop through the range of n and calculate the value of a[i]
    for i in range(1, n + 1):
        a.append(i * i - i + 1)

    # Initialize a counter to store the number of valid triples
    count = 0

    # Loop through the list of values of a and check if a[i] + a[j] + a[k] is a multiple of 3
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1

    # Return the number of valid triples
    return count

