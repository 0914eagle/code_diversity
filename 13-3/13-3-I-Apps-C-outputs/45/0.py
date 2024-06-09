
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
        if p <= len(coders.intersection([i + 1, i + 2])):
            suspects.add(i + 1)
            suspects.add(i + 2)
    # Return the number of possible two-suspect sets
    return len(suspects)

def f2(...):
    # Your code here

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    print(f1(n, p))

