
def solve(k, n):
    # Initialize variables
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    strings = []
    count = 0
    
    # Iterate through all possible strings
    for i in range(len(alphabet) ** k):
        # Convert the index to a binary string
        binary = bin(i)[2:]
        binary = binary.zfill(k)
        
        # Check if the string is double free
        double_free = True
        for j in range(k - 1):
            if binary[j] == binary[j + 1]:
                double_free = False
                break
        
        # Check if the string is k-incremental
        k_incremental = True
        for j in range(k):
            count = 0
            for c in binary:
                if c == str(j):
                    count += 1
            if count != j + 1:
                k_incremental = False
                break
        
        # If the string is double free and k-incremental, add it to the list
        if double_free and k_incremental:
            strings.append(binary)
    
    # Return the nth string in the list
    if n <= len(strings):
        return "".join(strings[n - 1])
    else:
        return -1

