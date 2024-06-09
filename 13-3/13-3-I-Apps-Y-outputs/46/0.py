
def get_staff_lines(n):
    staff_lines = []
    for i in range(n):
        staff_lines.append(" " * i + "*" * (n - i))
    return staff_lines

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

def get_staff_notation(notes):
    staff_lines = get_staff_lines(len(notes))
    for i, note in enumerate(notes):
        duration = get_note_duration(note)
        pitch = get_note_pitch(note)
        staff_lines[i] += pitch * duration
    return "\n".join(staff_lines)

def main():
    notes = input().split()
    print(get_staff_notation(notes))

if __name__ == '__main__':
    main()

