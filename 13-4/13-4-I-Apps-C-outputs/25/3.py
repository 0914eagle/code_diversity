
def get_min_instructions(program, num_banks, num_vars_per_bank):
    # Initialize the minimum number of instructions to 0
    min_instructions = 0
    # Initialize the current bank to 0
    current_bank = 0
    # Iterate through the program
    for instruction in program:
        # If the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            var_index = int(instruction[1:])
            # Calculate the bank for the variable
            bank = (var_index - 1) // num_vars_per_bank + 1
            # If the bank is different from the current bank
            if bank != current_bank:
                # Increment the minimum number of instructions
                min_instructions += 1
                # Set the current bank to the new bank
                current_bank = bank
        # If the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:instruction.find(" ")])
            # Get the program inside the repetition
            program_inside_repetition = instruction[instruction.find(" ")+1:-1]
            # Calculate the minimum number of instructions for the repetition
            min_instructions_repetition = get_min_instructions(program_inside_repetition, num_banks, num_vars_per_bank)
            # Increment the minimum number of instructions by the number of repetitions
            min_instructions += num_repetitions * min_instructions_repetition
    # Return the minimum number of instructions
    return min_instructions

def main():
    # Read the input
    num_banks, num_vars_per_bank = map(int, input().split())
    program = input().split()
    # Calculate the minimum number of instructions
    min_instructions = get_min_instructions(program, num_banks, num_vars_per_bank)
    # Print the minimum number of instructions
    print(min_instructions)

if __name__ == '__main__':
    main()

