
def output_number(n):
    instructions = []
    
    if n == 0:
        instructions.append("ZE A")
        instructions.append("DI A")
        return instructions
    
    while n > 0:
        instructions.append("ST A")
        instructions.append("PH A")
        instructions.append("AD")
        instructions.append("PL X")
        n -= 1
    
    instructions.append("DI X")
    
    return instructions

# Input
number = int(input())

# Output
instructions = output_number(number)
for instruction in instructions:
    print(instruction)
