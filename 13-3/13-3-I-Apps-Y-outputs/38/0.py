
def get_nop_instructions(program):
    # Initialize variables
    nop_instructions = 0
    current_address = 0

    # Iterate through the program
    for instruction in program:
        # Check if the instruction is uppercase (i.e., it is a new instruction)
        if instruction.isupper():
            # Check if the current address is divisible by 4
            if current_address % 4 == 0:
                # If it is, increment the current address by the number of parameters
                current_address += len(instruction) - 1
            else:
                # If it is not, calculate the number of NOP instructions needed to align the instruction
                nop_instructions += 4 - (current_address % 4)
                current_address += 4 - (current_address % 4)
        else:
            # If the instruction is lowercase (i.e., it is a parameter), increment the current address
            current_address += 1

    return nop_instructions

