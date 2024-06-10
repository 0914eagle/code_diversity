
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

def get_staff_line(note, staff_line):
    if note == "C":
        return staff_line[0]
    elif note == "D":
        return staff_line[1]
    elif note == "E":
        return staff_line[2]
    elif note == "F":
        return staff_line[3]
    elif note == "G":
        return staff_line[4]
    elif note == "A":
        return staff_line[5]
    elif note == "B":
        return staff_line[6]
    else:
        return staff_line[7]

def get_staff_lines(notes):
    staff_lines = []
    for note in notes:
        staff_line = get_staff_line(note[0], staff_line)
        staff_lines.append(staff_line)
    return staff_lines

def get_note_indices(notes):
    note_indices = []
    for note in notes:
        note_indices.append(get_note_duration(note))
    return note_indices

def get_notes_string(notes):
    notes_string = ""
    for note in notes:
        notes_string += get_note_pitch(note)
    return notes_string

def get_staff_string(notes):
    staff_lines = get_staff_lines(notes)
    notes_string = get_notes_string(notes)
    staff_string = ""
    for i in range(len(staff_lines)):
        staff_string += staff_lines[i] + "\n"
    staff_string += notes_string
    return staff_string

def main():
    notes = input("Enter the notes: ").split()
    notes_string = get_notes_string(notes)
    note_indices = get_note_indices(notes)
    staff_string = get_staff_string(notes)
    print(staff_string)

if __name__ == '__main__':
    main()

