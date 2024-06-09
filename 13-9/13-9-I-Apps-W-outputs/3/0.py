
def count_changed_bits(n, bits):
    changed_bits = 0
    for i in range(n):
        if bits[i] == "1":
            break
        changed_bits += 1
    return changed_bits

