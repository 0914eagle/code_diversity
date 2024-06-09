
def is_equivalent(program1, program2):
    # Convert the programs to lists of instructions
    instructions1 = program1.split()
    instructions2 = program2.split()

    # Check if the lists have the same length
    if len(instructions1) != len(instructions2):
        return "not equal"

    # Check if the instructions are the same
    for i in range(len(instructions1)):
        if instructions1[i] != instructions2[i]:
            return "not equal"

    # If all instructions are the same, the programs are equivalent
    return "equal"

