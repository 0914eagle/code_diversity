
def compare_dna_programs(program1, program2):
    # Initialize an empty string to store the result of applying the programs
    result1, result2 = "", ""
    
    # Iterate through the operations of both programs
    for op1, op2 in zip(program1, program2):
        # If the operations are the same, apply them to both strings
        if op1 == op2:
            result1, result2 = apply_operation(result1, op1), apply_operation(result2, op2)
        # If the operations are different, return False
        else:
            return False
    
    # If all operations are the same, return True
    return True

def apply_operation(string, operation):
    # Initialize an empty string to store the result of applying the operation
    result = ""
    
    # Iterate through the characters of the string
    for i, char in enumerate(string):
        # If the current character is not the one to be deleted, add it to the result
        if i != operation[1] - 1:
            result += char
    
    # If the operation is an insertion, insert the new character at the specified position
    if operation[0] == "I":
        result = result[:operation[1] - 1] + operation[2] + result[operation[1] - 1:]
    
    # Return the result of applying the operation
    return result

def main():
    # Read the input programs
    program1 = read_program()
    program2 = read_program()
    
    # Compare the programs and print the result
    if compare_dna_programs(program1, program2):
        print("0")
    else:
        print("1")

def read_program():
    # Read the number of operations
    n = int(input())
    
    # Initialize an empty list to store the operations
    program = []
    
    # Read the operations
    for i in range(n):
        operation = input().split()
        program.append(operation)
    
    # Return the list of operations
    return program

if __name__ == '__main__':
    main()

