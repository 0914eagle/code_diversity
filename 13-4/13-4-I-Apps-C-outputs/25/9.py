
def get_min_instructions(program):
    # Initialize variables
    min_instructions = 0
    banks = 1
    variables = 1
    bsr_value = None

    # Iterate through the program
    for instruction in program:
        # Check if the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])

            # Check if the variable index is within the range of the current banks and variables
            if variable_index <= banks * variables:
                # Increment the minimum instructions count
                min_instructions += 1
            else:
                # The variable index is out of range, set the BSR value
                bsr_value = variable_index // variables

                # Increment the minimum instructions count
                min_instructions += 2
        # Check if the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:])

            # Increment the minimum instructions count
            min_instructions += num_repetitions
        # Check if the instruction is an end of loop
        elif instruction == "E":
            # Check if the BSR value is set
            if bsr_value is not None:
                # Increment the minimum instructions count
                min_instructions += 1
        else:
            # The instruction is not recognized, raise an error
            raise ValueError("Invalid instruction: {}".format(instruction))

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

