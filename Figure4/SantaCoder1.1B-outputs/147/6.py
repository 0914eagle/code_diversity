def get_max_triples(n):
    
    a = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(a[i] for i in range(1, n) if a[i] % 3 == 0)


if __name__ == "__main__":
    print(get_max_triples(5))
    print(get_max_triples