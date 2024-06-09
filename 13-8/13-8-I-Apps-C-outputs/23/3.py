
def is_equivalent(program_a, program_b):
    # Convert the programs to lists of integers
    program_a_ints = [int(x) for x in program_a.split()]
    program_b_ints = [int(x) for x in program_b.split()]
    
    # Create a set of all possible output lists
    all_output_lists = set()
    for i in range(1, 10**9):
        all_output_lists.add(str(i))
    
    # Check if both programs have an equal probability of returning each possible output list
    for output_list in all_output_lists:
        probability_a = eval_program(program_a_ints, output_list)
        probability_b = eval_program(program_b_ints, output_list)
        if probability_a != probability_b:
            return "not equal"
    
    return "equal"

def eval_program(program, output_list):
    # Evaluate the program on the output list and return the probability of returning that list
    probability = 1
    for instruction in program:
        if instruction == "concat":
            probability *= eval_program(program[1:], output_list[len(program[1]):])
        elif instruction == "shuffle":
            probability *= 0.5
        elif instruction == "sorted":
            probability *= 1
    
    return probability

