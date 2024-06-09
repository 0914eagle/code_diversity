
def solve(n, k, batteries):
    batteries.sort()
    d = 10**9 + 1
    for i in range(2**n):
        mask = i
        total = 0
        for j in range(n):
            chip_power = 0
            for k in range(k):
                chip_power += batteries[mask % 2]
                mask //= 2
            total += chip_power
        d = min(d, abs(total - 2*chip_power))
    return d

