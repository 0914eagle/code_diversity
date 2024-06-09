
def get_min_instructions(program):
    # Initialize variables
    min_instructions = 0
    banks = 1
    variables = 1
    bsr_set = False

    # Iterate through the program
    for instruction in program:
        # Check if the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])

            # Check if the variable index is within the range of the current banks and variables
            if variable_index <= banks * variables:
                # Increment the minimum number of instructions
                min_instructions += 1
            else:
                # The variable index is out of range, so set the BSR and increment the minimum number of instructions
                bsr_set = True
                min_instructions += 2
        # Check if the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:])

            # Check if the BSR has been set
            if bsr_set:
                # Increment the minimum number of instructions
                min_instructions += num_repetitions
            else:
                # The BSR has not been set, so set it and increment the minimum number of instructions
                bsr_set = True
                min_instructions += num_repetitions + 1
        # Check if the instruction is an end of program marker
        elif instruction == "E":
            # Break out of the loop
            break

    # Return the minimum number of instructions
    return min_instructions

def main():
    # Read the input
    banks, variables = map(int, input().split())
    program = input().split()

    # Get the minimum number of instructions
    min_instructions = get_min_instructions(program)

    # Print the minimum number of instructions
    print(min_instructions)

if __name__ == '__main__':
    main()

