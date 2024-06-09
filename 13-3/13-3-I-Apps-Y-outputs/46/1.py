
def get_note_duration(note):
    if note.isdigit():
        return int(note)
    else:
        return 1

def get_note_pitch(note):
    if note.isdigit():
        return "*"
    else:
        return note

def get_staff_line(note, staff_size):
    if note == "C":
        return staff_size - 1
    elif note == "D":
        return staff_size - 2
    elif note == "E":
        return staff_size - 3
    elif note == "F":
        return staff_size - 4
    elif note == "G":
        return staff_size - 5
    elif note == "A":
        return staff_size - 6
    elif note == "B":
        return staff_size - 7
    else:
        return staff_size - 8

def get_staff_lines(notes, staff_size):
    staff_lines = []
    for note in notes:
        staff_lines.append(get_staff_line(note, staff_size))
    return staff_lines

def get_note_symbols(notes, staff_size):
    note_symbols = []
    for note in notes:
        note_symbols.append(get_note_pitch(note) * get_note_duration(note))
    return note_symbols

def get_staff(notes, staff_size):
    staff_lines = get_staff_lines(notes, staff_size)
    note_symbols = get_note_symbols(notes, staff_size)
    staff = []
    for i in range(staff_size):
        line = []
        for j in range(len(notes)):
            if staff_lines[j] == i:
                line.append(note_symbols[j])
        staff.append(" ".join(line))
    return "\n".join(staff)

def main():
    notes = input().split()
    staff_size = 5
    print(get_staff(notes, staff_size))

if __name__ == '__main__':
    main()

