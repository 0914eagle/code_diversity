
def output_number(n):
    instructions = []
    
    # Initialize registers A and X to 1
    instructions.append("ST A")
    instructions.append("ST X")
    
    # Convert the number to binary and push each bit onto the stack
    binary = format(n, '08b')
    for bit in binary:
        if bit == '1':
            instructions.append("ST Y")
            instructions.append("PH Y")
        else:
            instructions.append("ZE Y")
            instructions.append("PH Y")
    
    # Add the bits together
    while len(instructions) < 40:
        instructions.append("PL Y")
        instructions.append("PL X")
        instructions.append("AD")
        instructions.append("PH Y")
    
    # Display the result
    instructions.append("DI Y")
    
    return instructions

# Input the number to output
number = int(input())
instructions = output_number(number)
for instruction in instructions:
    print(instruction)
