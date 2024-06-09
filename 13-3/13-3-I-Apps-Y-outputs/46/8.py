
def get_note_duration(note):
    if note.isdigit():
        return int(note)
    else:
        return 1

def get_note_pitch(note):
    if note.isdigit():
        return "*" * get_note_duration(note)
    else:
        return "*"

def get_staff_line(notes):
    staff_line = ""
    for note in notes:
        staff_line += get_note_pitch(note)
    return staff_line

def get_staff(notes):
    staff = []
    for note in notes:
        staff.append(get_staff_line(note))
    return staff

def get_output(notes):
    staff = get_staff(notes)
    output = ""
    for line in staff:
        output += line + "\n"
    return output

def main():
    notes = input("Enter the notes: ").split()
    print(get_output(notes))

if __name__ == '__main__':
    main()

