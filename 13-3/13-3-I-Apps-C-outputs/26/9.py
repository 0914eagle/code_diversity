
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

    # If the number of plus crossings is equal to the number of minus crossings, the wires can be untangled
    if plus_crossings == minus_crossings:
        return "Yes"
    else:
        return "No"

