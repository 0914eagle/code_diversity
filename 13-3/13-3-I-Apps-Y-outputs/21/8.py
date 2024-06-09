
def solve(notes):
    # Initialize the staff with the five lines and the spaces between them
    staff = ["G:                                                            ",
             "F: -------------------------------------*-------------------- ",
             "E:       *   *          *             *   *                   ",
             "D: ----*-------**-----*-------------*-------*---------------- ",
             "C: * *     *      * *     **    * *           *         ** ** "]

    # Iterate through the notes and add them to the staff
    for note in notes:
        # Get the pitch and duration of the note
        pitch = note[0]
        duration = note[1] if len(note) == 2 else 1

        # Find the line and column where the note should be placed
        line = "ABCDEFG"[:staff.index(pitch)]
        column = staff.index(line) + 1

        # Add the note to the staff
        staff[line] = staff[line][:column] + "*" * duration + staff[line][column + 1:]

    return "\n".join(staff)

