
def solve(n):
    # The minimum number of packets is n
    packets = n
    # Loop through all possible values of x
    for x in range(1, n+1):
        # If x is not a multiple of n, we need one more packet
        if x % n != 0:
            packets += 1
    return packets

