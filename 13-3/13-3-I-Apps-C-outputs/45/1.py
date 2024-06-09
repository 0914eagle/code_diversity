
def f1(n, p):
    # Initialize a set to store the names of the coders
    coders = set()
    # Loop through each coder and add their names to the set
    for i in range(n):
        coders.add(i + 1)
    # Initialize a counter to store the number of possible two-suspect sets
    count = 0
    # Loop through each coder and their two named coders
    for i in range(n):
        for j in range(i + 1, n):
            # If both coders are named by the current coder, remove them from the set
            if i + 1 in coders and j + 1 in coders:
                coders.remove(i + 1)
                coders.remove(j + 1)
                # Increment the counter
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
    # Loop through each coder and their two named coders
    for i in range(n):
        for j in range(i + 1, n):
            # If both coders are named by the current coder, remove them from the set
            if i + 1 in coders and j + 1 in coders:
                coders.remove(i + 1)
                coders.remove(j + 1)
                # Increment the counter
                count += 1
    # Return the number of possible two-suspect sets
    return count

if __name__ == '__main__':
    n, p = map(int, input().split())
    print(f1(n, p))
    print(f2(n, p))

