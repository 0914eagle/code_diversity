
def output_number(n):
    instructions = []
    
    if n == 0:
        instructions.append("ZE A")
    else:
        while n > 0:
            if n % 2 == 1:
                instructions.append("ST A")
            instructions.append("PH A")
            instructions.append("PH X")
            instructions.append("AD")
            instructions.append("PL X")
            instructions.append("PL A")
            n //= 2
    
    instructions.append("DI A")
    
    return instructions

# Input
N = int(input())
# Output
for instruction in output_number(N):
    print(instruction)
