
def get_min_instructions(banks, variables, program):
    # Initialize the minimum number of instructions to 0
    min_instructions = 0
    # Initialize the current bank to 0
    current_bank = 0
    # Iterate through the program
    for instruction in program:
        # If the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])
            # Get the bank for the variable
            bank = (variable_index - 1) // variables + 1
            # If the bank is different from the current bank
            if bank != current_bank:
                # Increment the minimum number of instructions
                min_instructions += 1
                # Set the current bank to the new bank
                current_bank = bank
        # If the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:])
            # Increment the minimum number of instructions
            min_instructions += num_repetitions
    # Return the minimum number of instructions
    return min_instructions

def main():
    # Read the input
    banks, variables = map(int, input().split())
    program = input().split()
    # Get the minimum number of instructions
    min_instructions = get_min_instructions(banks, variables, program)
    # Print the minimum number of instructions
    print(min_instructions)

if __name__ == '__main__':
    main()

