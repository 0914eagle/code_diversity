
def convert_number_to_instructions(num):
    instructions = []
    
    # Initialize registers A and X to 1
    instructions.append("ST A")
    instructions.append("ST X")
    
    # Convert the number to binary
    binary_num = bin(num)[2:].zfill(8)
    
    # Push each bit of the binary number onto the stack
    for bit in binary_num:
        if bit == '1':
            instructions.append("ST Y")
        instructions.append("PH Y")
    
    # Add all the bits together
    instructions.append("ZE Y")
    for _ in range(8):
        instructions.append("PH Y")
        instructions.append("AD")
    
    # Display the result
    instructions.append("DI Y")
    
    return instructions

# Input
num = int(input())

# Convert the number to instructions
instructions = convert_number_to_instructions(num)

# Output the instructions
for instruction in instructions:
    print(instruction)
