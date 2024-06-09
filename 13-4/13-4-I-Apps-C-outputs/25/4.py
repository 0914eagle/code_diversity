
def get_min_instructions(program):
    # Initialize variables
    min_instructions = 0
    bsr_value = None
    variable_map = {}

    # Iterate through the program
    for instruction in program:
        # If the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])

            # If the variable has not been referenced before
            if variable_index not in variable_map:
                # Increment the minimum number of instructions
                min_instructions += 1

                # Set the variable map
                variable_map[variable_index] = bsr_value
        # If the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:])

            # Increment the minimum number of instructions
            min_instructions += num_repetitions
        # If the instruction is a loop
        elif instruction == "E":
            # Break the loop
            break
        # If the instruction is a BSR setter
        elif instruction.startswith("BSR"):
            # Get the new BSR value
            new_bsr_value = int(instruction[3:])

            # If the BSR value has changed
            if new_bsr_value != bsr_value:
                # Increment the minimum number of instructions
                min_instructions += 1

                # Set the new BSR value
                bsr_value = new_bsr_value

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

