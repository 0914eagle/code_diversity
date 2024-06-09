
def get_max_triples(n: int) -> int:
    
    # Initialize an empty list to store the values of a
    a = []

    # Loop through the range of n and calculate the value of a[i]
    for i in range(1, n + 1):
        a.append(i * i - i + 1)

    # Initialize a counter to store the number of triples
    count = 0

    # Loop through the list of a and check if the sum of any three consecutive elements is a multiple of 3
    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1

    return count

