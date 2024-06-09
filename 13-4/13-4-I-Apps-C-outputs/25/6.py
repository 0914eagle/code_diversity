
def get_min_instructions(program):
    # Initialize variables
    min_instructions = 0
    bank_select_register = 0
    variable_map = {}

    # Iterate through the program
    for instruction in program:
        # Check if the instruction is a variable reference
        if instruction.startswith("V"):
            # Get the variable index
            variable_index = int(instruction[1:])

            # Check if the variable is already mapped to a bank
            if variable_index in variable_map:
                # If the variable is already mapped, get the bank index
                bank_index = variable_map[variable_index]
            else:
                # If the variable is not mapped, map it to the next available bank
                bank_index = bank_select_register
                variable_map[variable_index] = bank_index
                bank_select_register += 1

            # Increment the minimum instructions count
            min_instructions += 1

        # Check if the instruction is a repetition
        elif instruction.startswith("R"):
            # Get the number of repetitions
            num_repetitions = int(instruction[1:])

            # Increment the minimum instructions count
            min_instructions += num_repetitions

        # Check if the instruction is an end of program marker
        elif instruction == "E":
            # Break out of the loop
            break

    # Return the minimum instructions count
    return min_instructions

def main():
    # Read the input
    b, s = map(int, input().split())
    program = input().split()

    # Get the minimum instructions count
    min_instructions = get_min_instructions(program)

    # Print the result
    print(min_instructions)

if __name__ == '__main__':
    main()

