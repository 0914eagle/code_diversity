

def get_max_triples(n):
    
    # Initialize an array to store the values of a
    a = [None] * n

    # Fill the array with the desired values
    for i in range(n):
        a[i] = i * i - i + 1

    # Initialize a variable to store the number of triples
    count = 0

    # Loop through the array and check for triples that are multiples of 3
    for i in range(n-1):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] % 3 == 0:
                    count += 1

    return count

