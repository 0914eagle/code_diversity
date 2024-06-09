
def untangle_wires(wire_sequence):
    # Initialize variables to keep track of the number of crossings
    num_crossings = 0
    # Iterate through the wire sequence
    for i in range(len(wire_sequence) - 1):
        # If the current wire is plus and the next wire is minus, there is a crossing
        if wire_sequence[i] == "+" and wire_sequence[i + 1] == "-":
            num_crossings += 1
    # If there is an odd number of crossings, the wires cannot be untangled
    if num_crossings % 2 == 1:
        return "No"
    else:
        return "Yes"

