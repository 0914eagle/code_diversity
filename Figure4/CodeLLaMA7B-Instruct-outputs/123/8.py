

def get_odd_collatz(n):
    
    if n <= 0:
        return []

    collatz_seq = [n]
    while collatz_seq[-1] != 1:
        if collatz_seq[-1] % 2 == 0:
            collatz_seq.append(collatz_seq[-1] // 2)
        else:
            collatz_seq.append(3 * collatz_seq[-1] + 1)

    return sorted([x for x in collatz_seq if x % 2 != 0])


