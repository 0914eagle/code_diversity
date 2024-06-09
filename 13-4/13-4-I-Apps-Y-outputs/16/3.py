
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

def get_staff_line(note):
    pitch = get_note_pitch(note)
    duration = get_note_duration(note)
    return pitch * duration

def get_staff_lines(notes):
    staff_lines = []
    for note in notes:
        staff_line = get_staff_line(note)
        staff_lines.append(staff_line)
    return staff_lines

def get_staff(notes):
    staff_lines = get_staff_lines(notes)
    staff = "\n".join(staff_lines)
    return staff

def main():
    notes = input("Enter the notes: ")
    staff = get_staff(notes)
    print(staff)

if __name__ == "__main__":
    main()

