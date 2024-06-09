
def convert_to_staff_notation(notes):
    staff = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]
    note_values = ["*", "**", "***", "****", "*****"]
    note_duration = 1
    note_count = 0
    staff_output = []
    for note in notes:
        if note.isupper():
            note_duration = 1
        elif note.isdigit():
            note_duration = int(note)
        else:
            note_count += 1
            staff_output.append(staff[note_count % 7] + " " * (note_count // 7) + note_values[note_duration - 1])
    return "\n".join(staff_output)

def main():
    notes = input("Enter the notes: ").split()
    print(convert_to_staff_notation(notes))

if __name__ == '__main__':
    main()

