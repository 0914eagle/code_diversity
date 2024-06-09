
def count_critical_cpus(n, m, k, blocks):
    # Initialize a 3D array to represent the state of the CPUs
    cpu_state = [[[False] * k for _ in range(m)] for _ in range(n)]

    # Parse the input blocks and set the state of the CPUs
    for i, block in enumerate(blocks):
        for j, line in enumerate(block.splitlines()):
            for k, char in enumerate(line):
                if char == "1":
                    cpu_state[i][j][k] = True

    # Initialize a set to store the critical CPUs
    critical_cpus = set()

    # Iterate over each CPU and check if it is critical
    for i in range(n):
        for j in range(m):
            for k in range(k):
                # If the CPU is malfunctioning, skip it
                if not cpu_state[i][j][k]:
                    continue

                # Check if the CPU controls any other CPUs
                for x in range(i, n):
                    for y in range(j, m):
                        for z in range(k, k):
                            # If the CPU controls another CPU, add it to the set of critical CPUs
                            if cpu_state[x][y][z] and (x, y, z) != (i, j, k):
                                critical_cpus.add((i, j, k))
                                break

    return len(critical_cpus)

