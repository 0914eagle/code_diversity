
def is_equivalent(program1, program2):
    # Convert the programs to lists of integers
    program1_ints = [int(x) for x in program1.split()]
    program2_ints = [int(x) for x in program2.split()]
    # Check if the lists are the same length
    if len(program1_ints) != len(program2_ints):
        return "not equal"
    # Check if the lists contain the same integers
    for i in range(len(program1_ints)):
        if program1_ints[i] != program2_ints[i]:
            return "not equal"
    # If the lists are the same, the programs are equivalent
    return "equal"

