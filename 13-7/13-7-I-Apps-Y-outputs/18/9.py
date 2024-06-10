
def convert_to_notation(notes):
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

    # Convert the notes to the staff notation
    for note in notes:
        # Get the pitch and duration of the note
        pitch = note[0]
        duration = note[1] if len(note) > 1 else 1

        # Find the line and column of the note on the staff
        line = "GDEFABCgfe"[pitch.upper()]
        column = 2 if pitch.isupper() else 1

        # Print the note on the staff
        staff[line] = staff[line][:column] + "*" * duration + staff[line][column + 1:]

    return "\n".join(staff)

def main():
    # Read the input notes from stdin
    notes = input().split()

    # Convert the notes to the staff notation
    staff = convert_to_notation(notes)

    # Print the staff notation to stdout
    print(staff)

if __name__ == '__main__':
    main()

