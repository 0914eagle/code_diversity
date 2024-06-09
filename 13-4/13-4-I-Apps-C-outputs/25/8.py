
def get_min_instructions(program):
    # Initialize variables
    min_instructions = 0
    bank_select_register = 0
    variable_map = {}

    # Iterate through the program
    for instruction in program:
        # If the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])

            # If the variable is not already mapped to a bank
            if variable_index not in variable_map:
                # Map the variable to the current bank select register
                variable_map[variable_index] = bank_select_register

            # Increment the minimum number of instructions
            min_instructions += 1

        # If the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:])

            # Iterate through the repetitions
            for _ in range(num_repetitions):
                # Increment the minimum number of instructions
                min_instructions += 1

        # If the instruction is an end of loop instruction
        elif instruction == "E":
            # Increment the bank select register
            bank_select_register += 1

    # Return the minimum number of instructions
    return min_instructions

def main():
    # Read the input
    b, s = map(int, input().split())
    program = input().split()

    # Get the minimum number of instructions
    min_instructions = get_min_instructions(program)

    # Print the result
    print(min_instructions)

if __name__ == '__main__':
    main()

