
def generate_instructions(n):
    instructions = []
    
    # Initialize registers A and X to 1
    instructions.append("ST A")
    instructions.append("ST X")
    
    # Convert number to binary and push bits onto stack
    binary = format(n, '08b')
    for bit in binary:
        if bit == '1':
            instructions.append("ST Y")
        instructions.append("PH Y")
    
    # Add all bits together
    instructions.append("ZE A")
    instructions.append("ZE X")
    instructions.append("PH A")
    instructions.append("PH X")
    instructions.append("AD")
    instructions.append("PL Y")
    
    # Display result
    instructions.append("DI Y")
    
    return instructions

# Input number to display
number = int(input())
instructions = generate_instructions(number)

for instruction in instructions:
    print(instruction)
