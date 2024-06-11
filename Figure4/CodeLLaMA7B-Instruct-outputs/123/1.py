

def get_odd_collatz(n):
    
    if n <= 0:
        return []

    collatz_seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_seq.append(n)

    return sorted([x for x in collatz_seq if x % 2 != 0])


