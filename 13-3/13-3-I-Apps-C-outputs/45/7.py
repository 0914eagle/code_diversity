
def f1(n, p):
    # Initialize a set to store the names of the coders
    coders = set()
    # Loop through each coder and add their names to the set
    for i in range(n):
        coders.add(i + 1)
    # Initialize a set to store the names of the suspects
    suspects = set()
    # Loop through each coder and add their names to the set if they agreed with the head's choice
    for i in range(n):
        if p <= len(coders.intersection({i + 1, coders[i]})):
            suspects.add(i + 1)
    # Return the number of possible two-suspect sets
    return len(suspects)

def f2(n, p):
    # Initialize a set to store the names of the coders
    coders = set()
    # Loop through each coder and add their names to the set
    for i in range(n):
        coders.add(i + 1)
    # Initialize a set to store the names of the suspects
    suspects = set()
    # Loop through each coder and add their names to the set if they agreed with the head's choice
    for i in range(n):
        if p <= len(coders.intersection({i + 1, coders[i]})):
            suspects.add(i + 1)
    # Return the number of possible two-suspect sets
    return len(suspects)

if __name__ == '__main__':
    n, p = map(int, input().split())
    print(f1(n, p))
    print(f2(n, p))

