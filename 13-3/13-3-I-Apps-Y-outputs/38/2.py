
def get_nop_instructions(program):
    # Initialize variables
    nop_instructions = 0
    current_address = 0

    # Iterate through the program
    for instruction in program:
        # Check if the instruction is uppercase (i.e., it is an instruction)
        if instruction.isupper():
            # Check if the current address is divisible by 4
            if current_address % 4 == 0:
                # If it is, increment the current address by the number of parameters
                current_address += len(instruction)
            else:
                # If it is not, increment the number of NOP instructions needed
                nop_instructions += 1
                # Increment the current address by 1 (since NOP instructions take up 1 byte of memory)
                current_address += 1
        else:
            # If the instruction is lowercase (i.e., it is a parameter), increment the current address by 1
            current_address += 1

    return nop_instructions

