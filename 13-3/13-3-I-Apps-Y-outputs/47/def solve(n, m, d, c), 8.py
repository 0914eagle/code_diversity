
def solve(n, m, d, c):
    # Initialize the array a to store the sequence of river cells
    a = [0] * (n + 2)
    # Initialize the array p to store the positions of the platforms
    p = [0] * (m + 2)
    # Initialize the array j to store the positions of the jumps
    j = [0] * (n + 2)

    # Set the first platform at position 0 and the last platform at position n + 1
    p[1] = 0
    p[m + 1] = n + 1

    # Set the first jump at position 0
    j[0] = 0

    # Iterate through the platforms
    for i in range(1, m + 1):
        # Set the current platform at position p[i]
        current_platform = p[i]

        # Check if the current platform is within the range of the river
        if current_platform + c[i - 1] - 1 <= n:
            # Set the next platform at position p[i] + c[i - 1]
            p[i + 1] = current_platform + c[i - 1]

            # Check if the next platform is within the range of the river
            if p[i + 1] <= n:
                # Set the jump at position p[i + 1] - 1
                j[p[i + 1] - 1] = 1

                # Set the cell at position p[i + 1] - 1 to platform i
                a[p[i + 1] - 1] = i

    # Check if the last jump is within the range of the river
    if j[n] == 1:
        return "YES"
    else:
        return "NO"

