
def output_number(n):
    instructions = []
    
    # Clear registers A, X, Y
    instructions.append("ZE A")
    instructions.append("ZE X")
    instructions.append("ZE Y")
    
    # Convert number to binary string
    binary_str = format(n, '08b')
    
    # Load binary digits into registers A and X
    for i in range(8):
        if binary_str[i] == '1':
            instructions.append("ST A")
        instructions.append("PH A")
        instructions.append("PH X")
        instructions.append("AD")
    
    # Pop final result from stack to register Y
    instructions.append("PL Y")
    
    # Display the result
    instructions.append("DI Y")
    
    return instructions

# Input number to output
number = int(input())
instructions = output_number(number)

for instruction in instructions:
    print(instruction)
