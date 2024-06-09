
def get_note_duration(note):
    if note.isdigit():
        return int(note)
    else:
        return 1

def get_note_pitch(note):
    if note.isdigit():
        return " "
    else:
        return note

def get_staff_line(note_duration):
    if note_duration == 1:
        return "*"
    elif note_duration == 2:
        return "**"
    else:
        return "***"

def get_staff_lines(notes):
    staff_lines = []
    for note in notes:
        note_duration = get_note_duration(note)
        note_pitch = get_note_pitch(note)
        staff_line = get_staff_line(note_duration)
        staff_lines.append(staff_line)
    return staff_lines

def get_staff(notes):
    staff_lines = get_staff_lines(notes)
    staff = ""
    for staff_line in staff_lines:
        staff += staff_line + "\n"
    return staff

def main():
    notes = input("Enter the notes: ").split()
    staff = get_staff(notes)
    print(staff)

if __name__ == '__main__':
    main()

