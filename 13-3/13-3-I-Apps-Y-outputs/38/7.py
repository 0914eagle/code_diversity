
def solve(program):
    # Initialize variables
    nop_count = 0
    instruction_count = 0
    parameter_count = 0

    # Iterate through the program
    for char in program:
        # Check if the character is an instruction
        if char.isupper():
            instruction_count += 1
            parameter_count = 0
        # Check if the character is a parameter
        elif char.islower():
            parameter_count += 1
        # Check if the character is a NOP instruction
        elif char == "N":
            nop_count += 1

    # Calculate the smallest number of NOP instructions needed
    nop_needed = (4 - (instruction_count * 4 + parameter_count) % 4) % 4

    return nop_needed

