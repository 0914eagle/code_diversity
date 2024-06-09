
def f1(n, p):
    # Initialize a set to store the names of the coders
    coders = set()
    # Loop through each coder and add their names to the set
    for i in range(n):
        coders.add(i + 1)
    # Initialize a counter to store the number of possible two-suspect sets
    count = 0
    # Loop through each coder and consider them as the first suspect
    for i in range(n):
        # Initialize a set to store the names of the second suspects
        suspects = set()
        # Loop through each coder and add their names to the set if they agreed with the first suspect
        for j in range(n):
            if i + 1 in (j + 1, j + 2):
                suspects.add(j + 1)
        # If the number of agreed suspects is greater than or equal to p, increment the counter
        if len(suspects) >= p:
            count += 1
    # Return the number of possible two-suspect sets
    return count

def f2(n, p):
    # Initialize a set to store the names of the coders
    coders = set()
    # Loop through each coder and add their names to the set
    for i in range(n):
        coders.add(i + 1)
    # Initialize a counter to store the number of possible two-suspect sets
    count = 0
    # Loop through each coder and consider them as the first suspect
    for i in range(n):
        # Initialize a set to store the names of the second suspects
        suspects = set()
        # Loop through each coder and add their names to the set if they agreed with the first suspect
        for j in range(n):
            if i + 1 in (j + 1, j + 2):
                suspects.add(j + 1)
        # If the number of agreed suspects is greater than or equal to p, increment the counter
        if len(suspects) >= p:
            count += 1
    # Return the number of possible two-suspect sets
    return count

if __name__ == '__main__':
    n, p = map(int, input().split())
    print(f1(n, p))
    print(f2(n, p))

