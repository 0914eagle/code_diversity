
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

            # Check if the instruction has parameters
            if char.lower() in program:
                # Increment the parameter count
                parameter_count += 1

    # Calculate the number of NOP instructions needed
    nop_count = (4 - (instruction_count * 4 + parameter_count)) % 4

    return nop_count

