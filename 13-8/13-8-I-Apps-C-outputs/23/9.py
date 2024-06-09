
def is_equal(program1, program2):
    # Convert the programs to lists of integers
    program1_list = list(map(int, program1.split()))
    program2_list = list(map(int, program2.split()))
    
    # Check if the lengths of the lists are equal
    if len(program1_list) != len(program2_list):
        return "not equal"
    
    # Check if all the integers in both lists are equal
    for i in range(len(program1_list)):
        if program1_list[i] != program2_list[i]:
            return "not equal"
    
    # If all the checks pass, the programs are equal
    return "equal"

