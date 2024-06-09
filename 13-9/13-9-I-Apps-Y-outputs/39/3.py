
def get_safe_operations(registers):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    overflow_registers = [0, 0, 0, 0, 0, 0, 0, 0]
    total_operations = 0

    for i in range(len(registers)):
        register_value = registers[i]
        prime = prime_numbers[i]

        if register_value == prime - 1:
            overflow_registers[i] = 1
        else:
            total_operations += 1

    for i in range(len(overflow_registers)):
        if overflow_registers[i] == 1:
            total_operations -= 1
            if i == len(overflow_registers) - 1:
                break
            overflow_registers[i+1] = 1

    return total_operations

