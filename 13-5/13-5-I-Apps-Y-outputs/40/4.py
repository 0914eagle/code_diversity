
def get_number_of_machines(socks, capacity, max_color_diff):
    num_machines = 1
    current_machine_size = 0
    for sock in socks:
        if current_machine_size == capacity:
            num_machines += 1
            current_machine_size = 0
        current_machine_size += 1
    return num_machines

