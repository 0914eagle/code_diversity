
def washing_machines(socks, capacity, color_diff):
    # Sort the socks by color
    socks.sort()
    # Initialize the number of machines to 1
    machines = 1
    # Initialize the current machine with the first sock
    current_machine = [socks[0]]
    # Iterate over the remaining socks
    for sock in socks[1:]:
        # If the color difference between the current sock and the last sock in the machine is less than or equal to the maximum color difference, add the sock to the machine
        if abs(sock - current_machine[-1]) <= color_diff:
            current_machine.append(sock)
        # If the machine is full or the color difference is greater than the maximum color difference, start a new machine
        elif len(current_machine) == capacity:
            machines += 1
            current_machine = [sock]
        # If the machine is not full and the color difference is greater than the maximum color difference, start a new machine
        else:
            machines += 1
            current_machine = [sock]
    return machines

