
def create_staff(notes):
    staff = ["G:                                                            ",
             "F: -------------------------------------*-------------------- ",
             "E:       *   *          *             *   *                   ",
             "D: ----*-------**-----*-------------*-------*---------------- ",
             "C: * *     *      * *     **    * *           *         ** **",
             "B: --------------------------**-----------------*-----*------",
             "A:                                                  *         ",
             "g: -----------------------------------------------*----------",
             "f:                                                            ",
             "e: ----------------------------------------------------------",
             "d:                                                            ",
             "c:                                                            ",
             "b:                                                            ",
             "a: ----------------------------------------------------------"]

    for note in notes:
        pitch = note[0]
        duration = note[1] if len(note) == 2 else 1
        staff_line = staff[ord(pitch) - ord('A')]
        staff_line = staff_line[:staff_line.index('*') + duration] + '*' + staff_line[staff_line.index('*') + duration + 1:]
        staff[ord(pitch) - ord('A')] = staff_line

    return '\n'.join(staff)

