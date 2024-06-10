
def get_staff_lines(num_lines):
    staff_lines = []
    for i in range(num_lines):
        staff_lines.append("-" * 25)
    return staff_lines

def get_staff_notes(notes, staff_lines):
    staff_notes = []
    for note in notes:
        note_duration = note[1] if len(note) == 2 else 1
        note_pitch = note[0].lower()
        staff_line = staff_lines[ord(note_pitch) - ord("c")]
        staff_note = " " * (5 - note_duration) + "*" * note_duration
        staff_notes.append(staff_line.replace("-", staff_note, 1))
    return staff_notes

def print_staff(staff_notes):
    for note in staff_notes:
        print(note)

def main():
    num_notes = int(input())
    notes = input().split()
    staff_lines = get_staff_lines(5)
    staff_notes = get_staff_notes(notes, staff_lines)
    print_staff(staff_notes)

if __name__ == '__main__':
    main()

