
def get_number_of_machines(socks, capacity, max_color_diff):
    number_of_machines = 1
    current_machine_size = 0
    for sock in socks:
        if current_machine_size == capacity:
            number_of_machines += 1
            current_machine_size = 0
        current_machine_size += 1
        for other_sock in socks[sock + 1:]:
            if abs(sock - other_sock) <= max_color_diff:
                current_machine_size += 1
                break
    return number_of_machines

