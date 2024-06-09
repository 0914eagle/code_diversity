
def f1(s):
    # Function to calculate the average value of L(C) for a given sequence S
    # Initialize variables
    n = len(s)
    count = 0
    total = 0
    
    # Iterate over all possible sequences C represented by S
    for i in range(2**n):
        # Convert the binary representation of i to a sequence of H and T
        seq = []
        for j in range(n):
            if i & (1 << j):
                seq.append('H')
            else:
                seq.append('T')
        
        # Calculate the number of operations before Prof. Tuy stops
        count += 1
        for j in range(n):
            if seq[j] == 'H':
                total += j + 1
                break
    
    # Return the average value of L(C)
    return total / count

def f2(s):
    # Function to calculate the average value of L(C) for a given sequence S
    # Initialize variables
    n = len(s)
    count = 0
    total = 0
    
    # Iterate over all possible sequences C represented by S
    for i in range(2**n):
        # Convert the binary representation of i to a sequence of H and T
        seq = []
        for j in range(n):
            if i & (1 << j):
                seq.append('H')
            else:
                seq.append('T')
        
        # Calculate the number of operations before Prof. Tuy stops
        count += 1
        for j in range(n):
            if seq[j] == 'H':
                total += j + 1
                break
    
    # Return the average value of L(C)
    return total / count

if __name__ == '__main__':
    s = input()
    print(f1(s))

