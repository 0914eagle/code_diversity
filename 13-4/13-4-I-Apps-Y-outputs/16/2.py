
def convert_notation(notation):
    # Initialize the staff
    staff = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]

    # Iterate through the notation and add asterisks to the staff
    for note in notation:
        # Get the pitch and duration of the note
        pitch = note[0]
        duration = note[1] if len(note) > 1 else 1

        # Find the line and column of the note on the staff
        line = "GFEFEGDCB"[ord(pitch) - ord("C")]
        column = 2 * (duration - 1)

        # Add the asterisk to the staff
        staff[line] = staff[line][:column] + "*" + staff[line][column + 1:]

    # Return the staff as a string
    return "\n".join(staff)

