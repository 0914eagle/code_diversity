
def get_nop_count(program):
    # Initialize variables
    nop_count = 0
    instruction_count = 0
    parameter_count = 0

    # Iterate through the program
    for char in program:
        # Check if the character is an instruction
        if char.isupper():
            # Increment the instruction count
            instruction_count += 1

            # Check if the instruction is the first in the program
            if instruction_count == 1:
                # Check if the instruction is not at a memory address divisible by 4
                if instruction_count % 4 != 0:
                    # Increment the NOP count
                    nop_count += 1

        # Check if the character is a parameter
        elif char.islower():
            # Increment the parameter count
            parameter_count += 1

    # Return the NOP count
    return nop_count

