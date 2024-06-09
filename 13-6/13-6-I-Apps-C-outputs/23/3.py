
def f1(S):
    # Calculate the number of H and T in the sequence
    num_H = S.count('H')
    num_T = S.count('T')
    
    # Calculate the number of operations needed to turn over all H
    num_operations = num_H
    
    # If there are more T than H, add the number of operations needed to turn over all T
    if num_T > num_H:
        num_operations += num_T - num_H
    
    # Return the average number of operations
    return num_operations / len(S)

def f2(S):
    # Initialize the number of operations and the number of H and T
    num_operations = 0
    num_H = 0
    num_T = 0
    
    # Iterate through the sequence
    for c in S:
        # If the current character is H, increment the number of H
        if c == 'H':
            num_H += 1
        # If the current character is T, increment the number of T
        elif c == 'T':
            num_T += 1
        # If the current character is ?, add the number of operations needed to turn over all H and T
        elif c == '?':
            num_operations += num_H + num_T
    
    # Return the average number of operations
    return num_operations / len(S)

if __name__ == '__main__':
    S = input()
    print(f1(S))
    print(f2(S))

