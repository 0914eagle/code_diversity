
def convert_to_staff_notation(notes):
    staff = ["G:", "F:", "E:", "D:", "C:", "B:", "A:", "g:", "f:", "e:", "d:", "c:", "b:", "a:"]
    note_values = ["*", "**", "***", "****", "*****"]
    note_duration = 1
    staff_output = ""
    for note in notes:
        if note.isupper():
            staff_output += staff[note]
        else:
            staff_output += " " * (note_duration - 1) + note_values[note_duration - 1] + " "
            note_duration += 1
    return staff_output

def main():
    notes = input("Enter the notes: ")
    print(convert_to_staff_notation(notes))

if __name__ == '__main__':
    main()

