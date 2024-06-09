
def is_equivalent(program1, program2):
    # Convert the programs to lists of integers
    program1_list = list(map(int, program1.split()))
    program2_list = list(map(int, program2.split()))
    
    # Check if the programs have the same length
    if len(program1_list) != len(program2_list):
        return "not equal"
    
    # Check if the programs have the same integers in the same order
    for i in range(len(program1_list)):
        if program1_list[i] != program2_list[i]:
            return "not equal"
    
    # If the programs are equal, return "equal"
    return "equal"

