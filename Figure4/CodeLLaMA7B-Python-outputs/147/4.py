def get_max_triples(n):
    
    # Initialize the array
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # Initialize the count
    count = 0
    # Iterate over the array
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count


if __name__ == "__main__":
    n = 5
    print(get_max_triples(n))
