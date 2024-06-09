
def get_min_instructions(program):
    # Initialize variables
    min_instructions = 0
    banks = 1
    variables = 1
    bsr_value = None

    # Iterate through the program
    for instruction in program:
        # If the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])

            # If the variable index is not in the current bank
            if variable_index not in range(variables):
                # Increment the minimum instructions count
                min_instructions += 1

                # Set the new bank value
                banks = variable_index // variables + 1

                # Set the new variable value
                variables = variable_index % variables + 1

        # If the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the repetition count
            repetition_count = int(instruction[1:])

            # Increment the minimum instructions count
            min_instructions += repetition_count

        # If the instruction is an end of loop
        elif instruction == "E":
            # If the BSR value is not None
            if bsr_value is not None:
                # Increment the minimum instructions count
                min_instructions += 1

                # Set the new BSR value
                bsr_value = None

    # Return the minimum instructions count
    return min_instructions

def main():
    # Read the input
    banks, variables = map(int, input().split())
    program = input().split()

    # Get the minimum instructions count
    min_instructions = get_min_instructions(program)

    # Print the result
    print(min_instructions)

if __name__ == '__main__':
    main()

