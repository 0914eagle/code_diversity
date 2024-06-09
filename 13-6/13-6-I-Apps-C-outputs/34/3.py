
def f1(program1, program2):
    # Convert the programs to lists of operations
    program1 = program1.split()
    program2 = program2.split()
    
    # Initialize the string to be edited
    string = ""
    
    # Apply the operations in program1 to the string
    for operation in program1:
        if operation[0] == "D":
            # Delete the character at the given position
            string = string[:operation[1]-1] + string[operation[1]:]
        elif operation[0] == "I":
            # Insert the given character at the given position
            string = string[:operation[1]-1] + operation[2] + string[operation[1]-1:]
    
    # Apply the operations in program2 to the string
    for operation in program2:
        if operation[0] == "D":
            # Delete the character at the given position
            string = string[:operation[1]-1] + string[operation[1]:]
        elif operation[0] == "I":
            # Insert the given character at the given position
            string = string[:operation[1]-1] + operation[2] + string[operation[1]-1:]
    
    # Check if the strings are identical
    if string == "":
        return "0"
    else:
        return "1"

def f2(program1, program2):
    # Convert the programs to lists of operations
    program1 = program1.split()
    program2 = program2.split()
    
    # Initialize the string to be edited
    string = ""
    
    # Apply the operations in program1 to the string
    for operation in program1:
        if operation[0] == "D":
            # Delete the character at the given position
            string = string[:operation[1]-1] + string[operation[1]:]
        elif operation[0] == "I":
            # Insert the given character at the given position
            string = string[:operation[1]-1] + operation[2] + string[operation[1]-1:]
    
    # Apply the operations in program2 to the string
    for operation in program2:
        if operation[0] == "D":
            # Delete the character at the given position
            string = string[:operation[1]-1] + string[operation[1]:]
        elif operation[0] == "I":
            # Insert the given character at the given position
            string = string[:operation[1]-1] + operation[2] + string[operation[1]-1:]
    
    # Check if the strings are identical
    if string == "":
        return "0"
    else:
        return "1"

if __name__ == '__main__':
    program1 = input("Enter the first DNA editing program: ")
    program2 = input("Enter the second DNA editing program: ")
    print(f1(program1, program2))
    print(f2(program1, program2))

