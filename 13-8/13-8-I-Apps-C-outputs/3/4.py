
def solve(n):
    # Find the smallest number that is greater than or equal to the square root of n
    sqrt_n = int(n**0.5)

    # Initialize the number of packets to the smallest number that is greater than or equal to the square root of n
    num_packets = sqrt_n

    # Loop until the number of packets is less than or equal to n
    while num_packets <= n:
        # If the number of packets is a perfect square, return the number of packets
        if num_packets ** 0.5 == int(num_packets ** 0.5):
            return num_packets
        # Otherwise, increment the number of packets by 1 and try again
        num_packets += 1

    # If the number of packets exceeds n, return n
    return n

