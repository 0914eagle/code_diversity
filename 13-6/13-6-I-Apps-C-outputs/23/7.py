
def f1(s):
    # Function to calculate the average value of L(C) for a given sequence S
    # Initialize variables
    n = len(s)
    count = 0
    total = 0
    
    # Iterate over all possible sequences C represented by S
    for i in range(2**n):
        # Convert the binary representation of i to a sequence of H and T
        seq = ""
        for j in range(n):
            if i & (1 << j):
                seq += "H"
            else:
                seq += "T"
        
        # Calculate the number of operations before Prof. Tuy stops
        count += 1
        total += f2(seq)
    
    # Return the average value of L(C)
    return total / count

def f2(seq):
    # Function to calculate the number of operations before Prof. Tuy stops for a given sequence C
    # Initialize variables
    n = len(seq)
    count = 0
    
    # Iterate over the sequence C
    for i in range(n):
        # Check if there are exactly k > 0 coins showing H
        k = 0
        for j in range(i, n):
            if seq[j] == "H":
                k += 1
                break
        
        # If there are exactly k > 0 coins showing H, turn over the k-th coin from the left
        if k > 0:
            count += 1
            seq = seq[:i] + seq[i+k:]
            break
    
    # Return the number of operations before Prof. Tuy stops
    return count

if __name__ == '__main__':
    s = input()
    print(f1(s))

