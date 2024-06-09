
def f1(program1, program2):
    # Convert the programs to lists of operations
    program1_ops = program1.split()
    program2_ops = program2.split()
    
    # Check if the programs have the same number of operations
    if len(program1_ops) != len(program2_ops):
        return 1
    
    # Initialize an empty string for the current state of the DNA sequence
    current_seq = ""
    
    # Iterate through the operations of both programs
    for i in range(len(program1_ops)):
        # Check if the current operation is a Del operation
        if program1_ops[i][0] == "D":
            # Get the position of the character to delete
            pos = int(program1_ops[i][2:])
            
            # Delete the character at the given position
            current_seq = current_seq[:pos-1] + current_seq[pos:]
            
        # Check if the current operation is an Ins operation
        elif program1_ops[i][0] == "I":
            # Get the position to insert the character
            pos = int(program1_ops[i][2:program1_ops[i].find(" ")])
            # Get the character to insert
            char = program1_ops[i][program1_ops[i].find(" ")+1]
            
            # Insert the character at the given position
            current_seq = current_seq[:pos-1] + char + current_seq[pos-1:]
    
    # Check if the current state of the DNA sequence is the same for both programs
    if current_seq == "":
        return 0
    else:
        return 1

def f2(program1, program2):
    # Convert the programs to lists of operations
    program1_ops = program1.split()
    program2_ops = program2.split()
    
    # Check if the programs have the same number of operations
    if len(program1_ops) != len(program2_ops):
        return 1
    
    # Initialize an empty string for the current state of the DNA sequence
    current_seq = ""
    
    # Iterate through the operations of both programs
    for i in range(len(program1_ops)):
        # Check if the current operation is a Del operation
        if program1_ops[i][0] == "D":
            # Get the position of the character to delete
            pos = int(program1_ops[i][2:])
            
            # Delete the character at the given position
            current_seq = current_seq[:pos-1] + current_seq[pos:]
            
        # Check if the current operation is an Ins operation
        elif program1_ops[i][0] == "I":
            # Get the position to insert the character
            pos = int(program1_ops[i][2:program1_ops[i].find(" ")])
            # Get the character to insert
            char = program1_ops[i][program1_ops[i].find(" ")+1]
            
            # Insert the character at the given position
            current_seq = current_seq[:pos-1] + char + current_seq[pos-1:]
    
    # Check if the current state of the DNA sequence is the same for both programs
    if current_seq == "":
        return 0
    else:
        return 1

if __name__ == '__main__':
    program1 = input()
    program2 = input()
    
    print(f1(program1, program2))
    print(f2(program1, program2))

