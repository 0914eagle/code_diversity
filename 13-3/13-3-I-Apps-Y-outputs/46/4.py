
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

def get_staff_line(note):
    staff_line = ""
    for i in range(5):
        if i == 0:
            staff_line += "G:"
        elif i == 1:
            staff_line += "F:"
        elif i == 2:
            staff_line += "E:"
        elif i == 3:
            staff_line += "D:"
        elif i == 4:
            staff_line += "C:"
        staff_line += " " * 10
    return staff_line

def get_staff(notes):
    staff = ""
    for note in notes:
        staff += get_staff_line(note) + "\n"
    return staff

def main():
    notes = input().split()
    staff = get_staff(notes)
    print(staff)

if __name__ == '__main__':
    main()

