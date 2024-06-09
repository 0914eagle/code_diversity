
def expected_max_dots(m, n):
    return sum(i * (1/m) ** n for i in range(1, m+1))

