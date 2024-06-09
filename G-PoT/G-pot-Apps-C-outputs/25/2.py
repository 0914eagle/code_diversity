
def output_number(n):
    instructions = []
    instructions.append(f"ST A")
    instructions.append(f"ST X")
    instructions.append(f"PH A")
    instructions.append(f"PH X")
    
    while n > 0:
        instructions.append(f"AD")
        instructions.append(f"PL Y")
        n -= 1
    
    instructions.append(f"DI Y")
    
    return instructions

# Input
N = int(input())
output = output_number(N)

# Output
for instruction in output:
    print(instruction)
