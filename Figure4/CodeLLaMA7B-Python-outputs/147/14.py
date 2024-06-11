def get_max_triples(n):
    
    # Initialize a list of size n
    a = [0] * n
    # For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    for i in range(n):
        a[i] = i * i - i + 1
    # Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    # and a[i] + a[j] + a[k] is a multiple of 3.
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count


if __name__ == "__main__":
    n = 5
    print(get_max_triples(n))
