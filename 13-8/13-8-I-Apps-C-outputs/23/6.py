
def is_equivalent(program1, program2):
    # Convert the programs to lists of integers
    program1_ints = [int(x) for x in program1.split()]
    program2_ints = [int(x) for x in program2.split()]
    # Check if the two lists are equal
    return program1_ints == program2_ints

