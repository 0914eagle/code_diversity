
def solve(M, S, spell):
    # Initialize the maximum power that can be discharged
    max_power = 0
    # Initialize the string of no-ops
    no_ops = ""
    # Loop through each step in the spell
    for i in range(M):
        # Check if the current step is a + step
        if spell[i] == "+":
            # Add 1 to the power
            max_power += 1
        # Check if the current step is an x step
        elif spell[i] == "x":
            # Multiply the power by 2
            max_power *= 2
        # Check if the power exceeds the strength
        if max_power > S:
            # Subtract the power by the strength
            max_power -= S
        # Add a no-op to the string
        no_ops += "o"
    # Return the string of no-ops
    return no_ops

def main():
    # Read the input
    M, S, spell = map(int, input().split())
    spell = input()
    # Call the solve function
    no_ops = solve(M, S, spell)
    # Print the output
    print(no_ops)

if __name__ == '__main__':
    main()

