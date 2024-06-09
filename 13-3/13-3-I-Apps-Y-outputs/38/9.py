
def get_nop_instructions(program):
    # Initialize variables
    nop_instructions = 0
    instruction_count = 0
    parameter_count = 0

    # Iterate through the program
    for char in program:
        # Check if the character is an instruction
        if char.isupper():
            # Increment the instruction count
            instruction_count += 1

            # Check if the instruction has parameters
            if char.islower():
                # Increment the parameter count
                parameter_count += 1

        # Check if the character is a parameter
        elif char.islower():
            # Increment the parameter count
            parameter_count += 1

    # Calculate the number of NOP instructions needed
    nop_instructions = (4 - (instruction_count * 4 + parameter_count) % 4) % 4

    return nop_instructions

