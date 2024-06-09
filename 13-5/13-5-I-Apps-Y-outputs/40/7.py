
def washing_machines(socks, capacity, color_diff):
    # Calculate the maximum number of socks that can be washed together
    max_socks = max(socks) - min(socks)
    # Calculate the number of machines needed
    num_machines = (max_socks // capacity) + (max_socks % capacity > 0)
    return num_machines

