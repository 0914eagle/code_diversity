def get_max_triples(n):
    
    # Initialize the array
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    # Initialize the counter
    counter = 0
    # Iterate over the array
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    counter += 1
    return counter


if __name__ == "__main__":
    print(get_max_triples(5))
    print(get_max_triples(10))
