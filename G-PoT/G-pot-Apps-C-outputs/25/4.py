
def generate_instructions(number):
    instructions = []
    instructions.append("ST A")
    instructions.append("ST X")
    
    for i in range(8):
        bit = (number >> i) & 1
        if bit == 1:
            instructions.append("ST Y")
            instructions.append("PH Y")
            instructions.append("AD")
        instructions.append("PL Y")
    
    instructions.append("DI Y")
    
    return instructions

number = int(input())
instructions = generate_instructions(number)

for instruction in instructions:
    print(instruction)
