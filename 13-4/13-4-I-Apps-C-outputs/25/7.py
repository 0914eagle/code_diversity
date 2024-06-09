
def get_min_instructions(program):
    # Initialize variables
    min_instructions = 0
    bank_select_register = 0
    memory_banks = [[] for _ in range(b)]
    variables = [0] * s

    # Iterate through the program
    for instruction in program:
        # If the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])

            # Check if the variable is already in memory
            if variables[variable_index] != 0:
                # If the variable is already in memory, skip this instruction
                continue

            # Check if the bank select register is set
            if bank_select_register == 0:
                # If the bank select register is not set, set it to the first bank
                bank_select_register = 1

            # Get the bank index
            bank_index = (bank_select_register - 1) % b

            # Check if the bank is full
            if len(memory_banks[bank_index]) == s:
                # If the bank is full, set the bank select register to the next bank
                bank_select_register += 1
                bank_index = (bank_select_register - 1) % b

            # Add the variable to the bank
            memory_banks[bank_index].append(variable_index)
            variables[variable_index] = 1
            min_instructions += 1

        # If the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:])

            # Check if the bank select register is set
            if bank_select_register == 0:
                # If the bank select register is not set, set it to the first bank
                bank_select_register = 1

            # Get the bank index
            bank_index = (bank_select_register - 1) % b

            # Check if the bank is full
            if len(memory_banks[bank_index]) == s:
                # If the bank is full, set the bank select register to the next bank
                bank_select_register += 1
                bank_index = (bank_select_register - 1) % b

            # Add the repetition to the bank
            memory_banks[bank_index].append(num_repetitions)
            min_instructions += 1

    return min_instructions

def main():
    b, s = map(int, input().split())
    program = input().split()
    print(get_min_instructions(program))

if __name__ == '__main__':
    main()

