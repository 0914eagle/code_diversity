
def f1(n, p):
    # Initialize a set to store the names of the coders
    coders = set()
    # Iterate through the input list
    for i in range(n):
        # Add the names of the coders to the set
        coders.add(i + 1)
        coders.add(input()[1])
    # Initialize a counter to store the number of possible two-suspect sets
    count = 0
    # Iterate through the combinations of two coders
    for coder1, coder2 in combinations(coders, 2):
        # Initialize a set to store the names of the coders who agreed with the choice
        agreed = set()
        # Iterate through the input list
        for i in range(n):
            # If the current coder agreed with the choice, add their name to the set
            if input()[0] == coder1 or input()[1] == coder1:
                agreed.add(i + 1)
            if input()[0] == coder2 or input()[1] == coder2:
                agreed.add(i + 1)
        # If the number of agreed coders is greater than or equal to p, increment the counter
        if len(agreed) >= p:
            count += 1
    # Return the number of possible two-suspect sets
    return count

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    f1_output = f1(...)
    f2_output = f2(...)
    # Print the output
    print(f1_output)
    print(f2_output)

