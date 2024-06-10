
def dna_edit_distance(p1, p2):
    # Initialize an empty string
    string = ''
    
    # Iterate through the operations in program 1
    for op in p1:
        # If the operation is a deletion, remove the character at the given position
        if op[0] == 'D':
            string = string[:op[1]-1] + string[op[1]:]
        # If the operation is an insertion, insert the given character at the given position
        elif op[0] == 'I':
            string = string[:op[1]-1] + op[2] + string[op[1]-1:]
    
    # Initialize a set to store the characters in the string
    chars = set()
    
    # Iterate through the characters in the string
    for c in string:
        # If the character is not already in the set, add it
        if c not in chars:
            chars.add(c)
    
    # Initialize a set to store the operations in program 2
    ops = set()
    
    # Iterate through the operations in program 2
    for op in p2:
        # If the operation is a deletion, remove the character at the given position
        if op[0] == 'D':
            string = string[:op[1]-1] + string[op[1]:]
        # If the operation is an insertion, insert the given character at the given position
        elif op[0] == 'I':
            string = string[:op[1]-1] + op[2] + string[op[1]-1:]
        # Add the operation to the set
        ops.add(op)
    
    # If the sets of characters and operations are the same, the programs are identical
    if chars == set(string) and ops == set(p2):
        return 0
    # Otherwise, the programs are different
    else:
        return 1

def main():
    # Read the input
    p1 = []
    p2 = []
    while True:
        line = input()
        if line == 'E':
            break
        if line[0] == 'D':
            p1.append(('D', int(line[2:])))
        elif line[0] == 'I':
            p1.append(('I', int(line[2:line.index(' ')]), line[line.index(' ')+1]))
    while True:
        line = input()
        if line == 'E':
            break
        if line[0] == 'D':
            p2.append(('D', int(line[2:])))
        elif line[0] == 'I':
            p2.append(('I', int(line[2:line.index(' ')]), line[line.index(' ')+1]))
    
    # Compare the programs
    print(dna_edit_distance(p1, p2))

if __name__ == '__main__':
    main()

