
def output_number(n):
    instructions = []
    
    # Initialize registers A and X to 1
    instructions.append("ST A")
    instructions.append("ST X")
    
    # Convert the number to binary
    binary = bin(n)[2:].zfill(8)
    
    # Push each bit of the binary number onto the stack
    for bit in binary:
        if bit == '1':
            instructions.append("ST Y")
        instructions.append("PH X")
        instructions.append("AD")
    
    # Pop the final result from the stack and display it
    instructions.append("PL Y")
    instructions.append("DI Y")
    
    return instructions

# Input
N = int(input())
output = output_number(N)

for instruction in output:
    print(instruction)
