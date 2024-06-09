
def untangle_wires(wire_sequence):
    # Initialize variables to keep track of the wire positions
    plus_position = 0
    minus_position = 0
    plus_above_minus = 0

    # Iterate through the wire sequence
    for wire in wire_sequence:
        if wire == "+":
            plus_position += 1
        else:
            minus_position += 1

        # Check if the "plus" wire is above the "minus" wire
        if plus_position > minus_position:
            plus_above_minus += 1

    # Check if the wires can be untangled
    if plus_above_minus % 2 == 0:
        return "Yes"
    else:
        return "No"

