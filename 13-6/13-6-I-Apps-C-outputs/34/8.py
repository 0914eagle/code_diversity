
def f1(program1, program2):
    # Initialize an empty string to store the result of applying the two programs
    result1, result2 = "", ""
    
    # Iterate through the operations of both programs
    for op1, op2 in zip(program1, program2):
        # If the current operation is a Del operation, delete the character at the specified position in both results
        if op1[0] == "D":
            result1 = result1[:op1[1]-1] + result1[op1[1]:]
            result2 = result2[:op2[1]-1] + result2[op2[1]:]
        # If the current operation is an Ins operation, insert the specified character at the specified position in both results
        elif op1[0] == "I":
            result1 = result1[:op1[1]-1] + op1[2] + result1[op1[1]-1:]
            result2 = result2[:op2[1]-1] + op2[2] + result2[op2[1]-1:]
    
    # Return 0 if the results of applying the two programs are identical, 1 otherwise
    return result1 == result2

def f2(program1, program2):
    # Initialize an empty string to store the result of applying the first program
    result1 = ""
    
    # Iterate through the operations of the first program
    for op1 in program1:
        # If the current operation is a Del operation, delete the character at the specified position in the result
        if op1[0] == "D":
            result1 = result1[:op1[1]-1] + result1[op1[1]:]
        # If the current operation is an Ins operation, insert the specified character at the specified position in the result
        elif op1[0] == "I":
            result1 = result1[:op1[1]-1] + op1[2] + result1[op1[1]-1:]
    
    # Return 0 if the result of applying the first program is identical to the result of applying the second program, 1 otherwise
    return result1 == f1(program2, program1)

if __name__ == '__main__':
    # Read the input programs from stdin
    program1 = []
    while True:
        line = input()
        if line == "E":
            break
        op = line.split()
        program1.append(op)
    
    program2 = []
    while True:
        line = input()
        if line == "E":
            break
        op = line.split()
        program2.append(op)
    
    # Call the functions to compare the programs and print the result
    print(f1(program1, program2))
    print(f2(program1, program2))

