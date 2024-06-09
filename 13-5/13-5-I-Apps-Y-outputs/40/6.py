
def get_number_of_machines(socks, capacity, max_color_diff):
    number_of_machines = 1
    current_machine_size = 0
    for sock in socks:
        if current_machine_size == capacity:
            number_of_machines += 1
            current_machine_size = 0
        current_machine_size += 1
    return number_of_machines

