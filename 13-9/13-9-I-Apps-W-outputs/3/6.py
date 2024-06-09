
def get_changed_bits(n, cell_state):
    cell_state = list(cell_state)
    carry = 1
    changed_bits = 0
    for i in range(n-1, -1, -1):
        if cell_state[i] == "1" and carry == 1:
            cell_state[i] = "0"
            carry = 1
        elif cell_state[i] == "0" and carry == 1:
            cell_state[i] = "1"
            carry = 0
        if carry == 1:
            changed_bits += 1
    return changed_bits

