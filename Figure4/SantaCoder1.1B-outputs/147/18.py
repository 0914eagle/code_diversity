def get_max_triples(n):
    
    a = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(a[i] + a[j] + a[k] for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n))


if