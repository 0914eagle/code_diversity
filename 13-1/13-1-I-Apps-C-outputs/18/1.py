
def get_min_packets(n):
    # Initialize the number of packets to 1
    packets = 1
    # Loop through the numbers from 1 to n
    for i in range(1, n + 1):
        # If the current number is not divisible by the number of packets, increment the number of packets
        if n % i != 0:
            packets += 1
    return packets

