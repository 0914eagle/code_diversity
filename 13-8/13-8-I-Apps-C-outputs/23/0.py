
def is_equal(program1, program2):
    # Convert the programs to lists of integers
    program1_ints = [int(x) for x in program1.split()]
    program2_ints = [int(x) for x in program2.split()]
    # Check if the programs have the same length
    if len(program1_ints) != len(program2_ints):
        return "not equal"
    # Check if the programs have the same integers in the same order
    for i in range(len(program1_ints)):
        if program1_ints[i] != program2_ints[i]:
            return "not equal"
    # If the programs are the same, return "equal"
    return "equal"

