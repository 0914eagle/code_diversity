
def cut_stick(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            if i != j and i * j == n:
                count += 1
    return count

