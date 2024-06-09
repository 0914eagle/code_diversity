
def get_note_duration(note):
    if note.isdigit():
        return int(note)
    else:
        return 1

def get_note_pitch(note):
    if note.isdigit():
        return note
    else:
        return note.upper()

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

def print_staff(notes):
    staff_line = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]
    for note in notes:
        note_duration = get_note_duration(note)
        note_pitch = get_note_pitch(note)
        staff_line_index = get_staff_line(note_pitch, staff_line)
        print(staff_line_index, end="")
        for i in range(note_duration):
            print("*", end="")
        print()

notes = input().split()
print_staff(notes)

