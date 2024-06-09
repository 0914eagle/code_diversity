
def washing_machines(socks, capacity, max_color_diff):
    # Sort the socks by color
    socks.sort()
    # Initialize the number of machines to 1
    machines = 1
    # Initialize the current machine with the first sock
    current_machine = [socks[0]]
    # Iterate over the remaining socks
    for sock in socks[1:]:
        # Check if the current machine can take the sock
        if len(current_machine) < capacity and abs(current_machine[0] - sock) <= max_color_diff:
            # Add the sock to the current machine
            current_machine.append(sock)
        else:
            # Create a new machine and add the sock to it
            machines += 1
            current_machine = [sock]
    return machines

