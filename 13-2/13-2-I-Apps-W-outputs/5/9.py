
def solve(n, a):
    # Initialize the minimum energy required to reach each intersection
    m = [0] * (n + 1)

    # Loop through each shortcut
    for i in range(1, n + 1):
        # If the shortcut starts at intersection i
        if a[i - 1] == i:
            # The minimum energy required to reach intersection i is 1
            m[i] = 1
        # If the shortcut starts at some other intersection j
        else:
            # The minimum energy required to reach intersection i is the minimum of:
            # - The energy required to reach intersection j from intersection 1 plus the energy required to reach intersection i from intersection j
            # - The energy required to reach intersection i from intersection 1
            m[i] = min(m[a[i - 1]] + m[i], m[1])

    return m[n]

