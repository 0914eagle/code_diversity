
def get_lamp_states(n, k):
    # Initialize an array to store the lamp states
    lamp_states = [0] * (n + 1)

    # Iterate through each lamp and set its state
    for i in range(1, n + 1):
        lamp_states[i] = 1 if i % 2 == 0 else 0

    # Initialize a count to store the number of sets of k lamps that are on
    count = 0

    # Iterate through each possible combination of k lamps
    for i in range(1, 2 ** n):
        # Convert the binary representation of i to a list of lamp numbers
        lamps = [j for j in range(1, n + 1) if i // 2 ** j % 2 == 1]

        # Check if the current combination of lamps is a valid set
        if len(lamps) == k:
            # Initialize a flag to indicate if all lamps are on
            all_on = True

            # Iterate through each lamp in the current combination
            for j in lamps:
                # Check if the current lamp is on
                if lamp_states[j] == 0:
                    # If the current lamp is off, set the flag to False
                    all_on = False
                    break

            # If all lamps are on, increment the count
            if all_on:
                count += 1

    # Return the count modulo 998244353
    return count % 998244353

def main():
    # Read the input n and k
    n, k = map(int, input().split())

    # Call the get_lamp_states function and print the result
    print(get_lamp_states(n, k))

if __name__ == '__main__':
    main()

