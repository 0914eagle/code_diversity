
def get_note_duration(note):
    if note.isdigit():
        return int(note)
    else:
        return 1

def get_note_pitch(note):
    if note.isdigit():
        return note
    else:
        return note.lower()

def create_staff(notes):
    staff = []
    for note in notes:
        duration = get_note_duration(note)
        pitch = get_note_pitch(note)
        staff.append("*" * duration)
    return staff

def print_staff(staff):
    print("G:")
    print("F:", "-" * 25)
    print("E:", " " * 5, " ".join(staff[:5]))
    print("D:", "-" * 25)
    print("C:", " ".join(staff[5:10]))
    print("B:", "-" * 25)
    print("A:", " ".join(staff[10:15]))
    print("g:", "-" * 25)
    print("f:")
    print("e:", "-" * 25)
    print("d:")
    print("c:")
    print("b:")
    print("a:", "-" * 25)

def main():
    notes = input("Enter the notes: ").split()
    staff = create_staff(notes)
    print_staff(staff)

if __name__ == '__main__':
    main()

