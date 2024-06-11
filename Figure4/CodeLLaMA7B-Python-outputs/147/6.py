def get_max_triples(n):
    
    # initialize the array
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    # initialize the count
    count = 0
    # iterate over the array
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    count += 1
    return count


if __name__ == "__main__":
    n = 5
    print(get_max_triples(n))
