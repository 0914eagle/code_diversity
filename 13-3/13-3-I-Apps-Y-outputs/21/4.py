
def solve(notes):
    # Initialize the staff
    staff = ["G:                                                            ",
             "F: -------------------------------------*-------------------- ",
             "E:       *   *          *             *   *                   ",
             "D: ----*-------**-----*-------------*-------*---------------- ",
             "C: * *     *      * *     **    * *           *         ** ** ",
             "B: --------------------------**-----------------*-----*------ ",
             "A:                                                  *         ",
             "g: -----------------------------------------------*---------- ",
             "f:                                                            ",
             "e: ---------------------------------------------------------- ",
             "d:                                                            ",
             "c:                                                            ",
             "b:                                                            ",
             "a: ---------------------------------------------------------- "]

    # Iterate through the notes and print them on the staff
    for note in notes:
        # Get the pitch and duration of the note
        pitch = note[0]
        duration = note[1] if len(note) == 2 else 1

        # Find the line and column where the note should be printed
        line = staff.index(pitch)
        column = 2 + (duration - 1) * 2

        # Print the note on the staff
        staff[line] = staff[line][:column] + "*" + staff[line][column + 1:]

    # Return the staff as a string
    return "\n".join(staff)

