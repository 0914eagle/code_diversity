
def expected_max(m, n):
    total = 0
    for i in range(1, m+1):
        total += i * (1/m) ** n
    return total

