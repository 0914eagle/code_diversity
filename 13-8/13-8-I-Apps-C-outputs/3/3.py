
def min_packets(n):
    # Find the smallest power of 2 greater than or equal to n
    power = 1
    while power < n:
        power *= 2
    # Initialize the number of packets to the power of 2
    packets = power
    # Subtract 1 from the number of packets for each coin above 1
    for i in range(1, n):
        packets -= 1
    return packets

