
def get_changed_bits(n, cell_state):
    cell_state = [int(bit) for bit in cell_state]
    changed_bits = 0
    for i in range(n):
        if cell_state[i] == 1:
            cell_state[i] = 0
            changed_bits += 1
        else:
            break
    return changed_bits

