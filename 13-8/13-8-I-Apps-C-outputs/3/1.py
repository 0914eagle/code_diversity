
def get_min_packets(n):
    # Initialize the number of packets to 1
    packets = 1
    # Loop until the number of packets is greater than or equal to n
    while packets < n:
        # Increment the number of packets
        packets += 1
        # Check if the number of packets is a divisor of n
        if n % packets == 0:
            # If it is, return the number of packets
            return packets
    # If we reach this point, no divisor of n was found, so return the number of packets
    return packets

