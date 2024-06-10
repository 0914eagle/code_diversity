
def get_note_duration(note):
    if note.isdigit():
        return int(note)
    return 1

def get_note_name(note):
    return note.upper()

def get_note_position(note):
    return "GFEDCBAgfedcba"[:note.upper().index(note) + 1]

def get_note_staff(note):
    return "GFEDCBAgfedcba"[note.upper().index(note) + 1]

def get_note_symbol(note):
    return "*" * get_note_duration(note)

def get_note_line(note):
    return get_note_position(note) + get_note_symbol(note)

def get_staff_line(note):
    return get_note_staff(note) + ":" + " " * (5 - get_note_position(note).index(get_note_staff(note))) + get_note_line(note)

def get_staff_lines(notes):
    staff_lines = []
    for note in notes:
        staff_lines.append(get_staff_line(note))
    return staff_lines

def get_song_staff(notes):
    staff = []
    for line in get_staff_lines(notes):
        staff.append(line)
    return staff

def main():
    notes = input("Enter the notes: ").split()
    print("\n".join(get_song_staff(notes)))

if __name__ == '__main__':
    main()

