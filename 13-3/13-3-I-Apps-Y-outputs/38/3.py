
def get_nop_instructions(program):
    # Initialize variables
    nop_instructions = 0
    instruction_count = 0
    parameter_count = 0

    # Iterate through the program
    for i, char in enumerate(program):
        # Check if the current character is an instruction
        if char.isupper():
            # Increment the instruction count
            instruction_count += 1

            # Check if the current instruction is the last instruction in the program
            if i == len(program) - 1:
                # Increment the number of NOP instructions needed
                nop_instructions += 1

            # Check if the current instruction is not the last instruction in the program
            elif program[i + 1].isupper():
                # Increment the number of NOP instructions needed
                nop_instructions += 1

        # Check if the current character is a parameter
        elif char.islower():
            # Increment the parameter count
            parameter_count += 1

    # Return the number of NOP instructions needed
    return nop_instructions

