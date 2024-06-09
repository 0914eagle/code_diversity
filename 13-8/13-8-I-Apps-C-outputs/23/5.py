
def is_equivalent(program1, program2):
    # Convert the programs to lists of integers
    program1_ints = [int(x) for x in program1.split()]
    program2_ints = [int(x) for x in program2.split()]
    
    # Check if the lengths of the two lists are the same
    if len(program1_ints) != len(program2_ints):
        return "not equal"
    
    # Check if all the integers in both lists are the same
    for i in range(len(program1_ints)):
        if program1_ints[i] != program2_ints[i]:
            return "not equal"
    
    # If all checks pass, the two programs are equivalent
    return "equal"

