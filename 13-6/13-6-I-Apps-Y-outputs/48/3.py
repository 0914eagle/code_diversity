
def get_number_of_machines(socks, capacity, max_color_diff):
    num_machines = 1
    current_machine = 1
    for i in range(1, len(socks)):
        if abs(socks[i] - socks[i-1]) <= max_color_diff:
            current_machine += 1
        else:
            num_machines += 1
            current_machine = 1
    
    return num_machines

