
def untangle_wires(wire_sequence):
    # Initialize variables to keep track of the number of crossings
    plus_crossings = 0
    minus_crossings = 0

    # Iterate through the wire sequence
    for i in range(len(wire_sequence)):
        # If the current position is a plus crossing, increment the plus crossings count
        if wire_sequence[i] == "+":
            plus_crossings += 1
        # If the current position is a minus crossing, increment the minus crossings count
        elif wire_sequence[i] == "-":
            minus_crossings += 1

    # If the number of plus crossings is even and the number of minus crossings is odd, the wires can be untangled
    if plus_crossings % 2 == 0 and minus_crossings % 2 == 1:
        return "Yes"
    # Otherwise, the wires cannot be untangled
    else:
        return "No"

